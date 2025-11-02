import { defineStore } from 'pinia';
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  updateProfile,
} from 'firebase/auth';
import { auth } from '../config/firebase';
// Removed Firestore - using PostgreSQL via backend API instead

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    loading: false,
    error: null,
    isAuthenticated: false,
  }),

  getters: {
    currentUser: (state) => state.user,
    isLoggedIn: (state) => state.isAuthenticated,
  },

  actions: {
    async initialize() {
      return new Promise((resolve) => {
        onAuthStateChanged(auth, async (user) => {
          if (user) {
            // Fetch user data from PostgreSQL to get surveyCompleted status
            try {
              const response = await fetch(`http://localhost:5001/api/db/users/${user.uid}`);
              const userData = await response.json();
              
              this.user = {
                uid: user.uid,
                email: user.email,
                displayName: user.displayName,
                photoURL: user.photoURL,
                surveyCompleted: userData.surveyCompleted || false,
                surveyData: userData.surveyData || null
              };
              console.log('✅ Auth store initialized with survey status:', userData.surveyCompleted);
            } catch (error) {
              console.warn('⚠️ Could not fetch user data from database:', error.message);
              // Fallback to Firebase Auth data only
              this.user = {
                uid: user.uid,
                email: user.email,
                displayName: user.displayName,
                photoURL: user.photoURL,
                surveyCompleted: false, // Default to false if can't fetch
                surveyData: null
              };
            }
            this.isAuthenticated = true;
          } else {
            this.user = null;
            this.isAuthenticated = false;
          }
          resolve(user);
        });
      });
    },

    async login(email, password) {
      this.loading = true;
      this.error = null;
      try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        
        // Fetch user data from PostgreSQL to get surveyCompleted status
        try {
          const response = await fetch(`http://localhost:5001/api/db/users/${userCredential.user.uid}`);
          const userData = await response.json();
          
          this.user = {
            uid: userCredential.user.uid,
            email: userCredential.user.email,
            displayName: userCredential.user.displayName,
            photoURL: userCredential.user.photoURL,
            surveyCompleted: userData.surveyCompleted || false,
            surveyData: userData.surveyData || null
          };
          console.log('✅ Logged in with survey status:', userData.surveyCompleted);
        } catch (error) {
          console.warn('⚠️ Could not fetch user data from database:', error.message);
          // Fallback to Firebase Auth data only
          this.user = {
            uid: userCredential.user.uid,
            email: userCredential.user.email,
            displayName: userCredential.user.displayName,
            photoURL: userCredential.user.photoURL,
            surveyCompleted: false,
            surveyData: null
          };
        }
        
        this.isAuthenticated = true;
        return { success: true };
      } catch (error) {
        this.error = error.message;
        return { success: false, error: error.message };
      } finally {
        this.loading = false;
      }
    },

    async register(email, password, name) {
      this.loading = true;
      this.error = null;
      try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        
        // Update profile with display name
        await updateProfile(userCredential.user, { displayName: name });

        // User document created in PostgreSQL by useFirebaseAuth composable (onAuthStateChanged)
        // New users haven't completed survey yet
        this.user = {
          uid: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: name,
          photoURL: userCredential.user.photoURL,
          surveyCompleted: false, // New users need to complete survey
          surveyData: null
        };
        this.isAuthenticated = true;
        return { success: true };
      } catch (error) {
        this.error = error.message;
        return { success: false, error: error.message };
      } finally {
        this.loading = false;
      }
    },

    async logout() {
      this.loading = true;
      try {
        await signOut(auth);
        this.user = null;
        this.isAuthenticated = false;
        return { success: true };
      } catch (error) {
        this.error = error.message;
        return { success: false, error: error.message };
      } finally {
        this.loading = false;
      }
    },

    async updateUserPreferences(preferences) {
      if (!this.user) return { success: false, error: 'Not authenticated' };

      // Update preferences via PostgreSQL backend (if needed in future)
      // For now just update local state
      if (!this.user.preferences) {
        this.user.preferences = {};
      }
      this.user.preferences = { ...this.user.preferences, ...preferences };
      return { success: true };
    },

    async markSurveyCompleted() {
      if (!this.user) return;
      
      // Update local state immediately for responsive UI
      this.user.surveyCompleted = true;
      
      // Note: The survey data is saved via SurveyPage.vue when user submits
      // This method is just for marking it completed in other contexts
      console.log('✅ Survey marked as completed');
    },
  },
});
