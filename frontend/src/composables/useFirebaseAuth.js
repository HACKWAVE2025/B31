import { ref, computed } from 'vue';
import { 
  getAuth,
  createUserWithEmailAndPassword, 
  signInWithEmailAndPassword, 
  signInWithPopup,
  GoogleAuthProvider,
  signOut,
  sendPasswordResetEmail,
  updateProfile,
  onAuthStateChanged
} from 'firebase/auth';
import { initializeApp, getApps } from 'firebase/app';
import axios from 'axios';

// Firebase configuration
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID
};

// Initialize Firebase - Check if already initialized to prevent duplicate app error
const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();

// Global state
const currentUser = ref(null);
const isLoading = ref(true);

// Listen to auth state changes
onAuthStateChanged(auth, async (user) => {
  isLoading.value = false;
  
  // Sync with PostgreSQL database when user logs in (skip if backend offline)
  if (user) {
    try {
      // First, ensure user exists in database (create or update)
      await axios.post('http://localhost:5001/api/db/users', {
        id: user.uid,
        email: user.email,
        displayName: user.displayName || user.email.split('@')[0]
      }, {
        timeout: 3000 // 3 second timeout
      });
      console.log('✅ User synced to PostgreSQL:', user.uid);
      
      // Then, fetch the full user data including surveyCompleted status
      const userDataResponse = await axios.get(`http://localhost:5001/api/db/users/${user.uid}`, {
        timeout: 3000
      });
      
      // Merge Firebase Auth data with PostgreSQL data
      currentUser.value = {
        ...user,
        surveyCompleted: userDataResponse.data.surveyCompleted || false,
        surveyData: userDataResponse.data.surveyData || null
      };
      console.log('✅ User data fetched - Survey completed:', userDataResponse.data.surveyCompleted);
    } catch (error) {
      // Silently fail if backend is not running - auth still works
      if (error.code === 'ECONNREFUSED' || error.code === 'ERR_NETWORK') {
        console.warn('⚠️ Backend offline - user auth works, but data not synced to PostgreSQL');
        currentUser.value = user;
      } else {
        console.error('❌ Failed to sync user to database:', error.message);
        currentUser.value = user;
      }
    }
  } else {
    currentUser.value = null;
  }
});

export function useFirebaseAuth() {
  // Validation helpers
  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const validatePassword = (password) => {
    const passwordRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;
    return passwordRegex.test(password);
  };

  const getPasswordErrors = (password) => {
    const errors = [];
    if (password.length < 8) errors.push("At least 8 characters");
    if (!/\d/.test(password)) errors.push("At least one number");
    if (!/[!@#$%^&*]/.test(password)) errors.push("At least one special character (!@#$%^&*)");
    return errors;
  };

  // Sign up with email and password
  const signUp = async (name, email, password) => {
    try {
      console.log('🔵 Creating user account...');
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      console.log('✅ User created:', userCredential.user.uid);
      
      await updateProfile(userCredential.user, {
        displayName: name
      });
      console.log('✅ Profile updated with name:', name);

      // Sync to PostgreSQL
      try {
        await axios.post('http://localhost:5001/api/db/users', {
          id: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: name
        });
        console.log('✅ User synced to database');
      } catch (dbError) {
        console.warn('⚠️ Database sync failed (auth still works):', dbError.message);
      }

      return { success: true, user: userCredential.user };
    } catch (error) {
      console.error('❌ Sign-up error:', error);
      let errorMessage = "Something went wrong. Please try again.";
      
      if (error.code === 'auth/email-already-in-use') {
        errorMessage = "Account already exists with this email.";
      } else if (error.code === 'auth/invalid-email') {
        errorMessage = "Invalid email address.";
      } else if (error.code === 'auth/weak-password') {
        errorMessage = "Password is too weak. Use at least 8 characters with numbers and special characters.";
      } else if (error.code === 'auth/operation-not-allowed') {
        errorMessage = "Email/password sign-up is not enabled. Please contact support.";
      }
      
      return { success: false, error: errorMessage };
    }
  };

  // Sign in with email and password
  const signIn = async (email, password) => {
    try {
      console.log('🔵 Signing in user...');
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      console.log('✅ Sign-in successful:', userCredential.user.email);
      return { success: true, user: userCredential.user };
    } catch (error) {
      console.error('❌ Sign-in error:', error);
      let errorMessage = "Invalid email or password.";
      
      if (error.code === 'auth/user-not-found') {
        errorMessage = "No account found with this email.";
      } else if (error.code === 'auth/wrong-password') {
        errorMessage = "Invalid email or password.";
      } else if (error.code === 'auth/invalid-email') {
        errorMessage = "Invalid email address.";
      } else if (error.code === 'auth/user-disabled') {
        errorMessage = "This account has been disabled.";
      } else if (error.code === 'auth/invalid-credential') {
        errorMessage = "Invalid email or password.";
      } else if (error.code === 'auth/too-many-requests') {
        errorMessage = "Too many failed attempts. Please try again later.";
      }
      
      return { success: false, error: errorMessage };
    }
  };

  // Sign in with Google
  const signInWithGoogle = async () => {
    try {
      // Configure Google provider
      googleProvider.setCustomParameters({
        prompt: 'select_account'
      });
      
      console.log('🔵 Initiating Google sign-in...');
      const result = await signInWithPopup(auth, googleProvider);
      console.log('✅ Google sign-in successful:', result.user.email);
      
      // Sync to PostgreSQL
      try {
        await axios.post('http://localhost:5001/api/db/users', {
          id: result.user.uid,
          email: result.user.email,
          displayName: result.user.displayName
        });
        console.log('✅ User synced to database');
      } catch (dbError) {
        console.warn('⚠️ Database sync failed (auth still works):', dbError.message);
      }

      return { success: true, user: result.user };
    } catch (error) {
      console.error('❌ Google sign-in error:', error);
      let errorMessage = "Failed to sign in with Google.";
      
      if (error.code === 'auth/popup-closed-by-user') {
        errorMessage = "Sign in popup was closed.";
      } else if (error.code === 'auth/cancelled-popup-request') {
        errorMessage = "Sign in was cancelled.";
      } else if (error.code === 'auth/popup-blocked') {
        errorMessage = "Popup was blocked by browser. Please allow popups for this site.";
      } else if (error.code === 'auth/unauthorized-domain') {
        errorMessage = "This domain is not authorized for Google sign-in. Please add it in Firebase Console.";
      } else if (error.code === 'auth/operation-not-allowed') {
        errorMessage = "Google sign-in is not enabled. Please enable it in Firebase Console.";
      }
      
      return { success: false, error: errorMessage };
    }
  };

  // Send password reset email
  const resetPassword = async (email) => {
    try {
      await sendPasswordResetEmail(auth, email);
      return { 
        success: true, 
        message: "If this email exists, a password reset link has been sent." 
      };
    } catch (error) {
      return { 
        success: false, 
        error: "Failed to send reset email. Please try again." 
      };
    }
  };

  // Sign out
  const logout = async () => {
    try {
      await signOut(auth);
      return { success: true };
    } catch (error) {
      return { success: false, error: "Failed to sign out." };
    }
  };

  return {
    // State
    currentUser: computed(() => currentUser.value),
    isLoading: computed(() => isLoading.value),
    isAuthenticated: computed(() => !!currentUser.value),
    
    // Methods
    signUp,
    signIn,
    signInWithGoogle,
    resetPassword,
    logout,
    validateEmail,
    validatePassword,
    getPasswordErrors
  };
}
