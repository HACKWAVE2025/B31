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
            // Using Firebase Auth only - user data synced to PostgreSQL by useFirebaseAuth
            this.user = {
              uid: user.uid,
              email: user.email,
              displayName: user.displayName,
              photoURL: user.photoURL,
            };
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
        // User data synced to PostgreSQL by useFirebaseAuth composable
        this.user = {
          uid: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: userCredential.user.displayName,
          photoURL: userCredential.user.photoURL,
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

    async register(email, password, name) {
      this.loading = true;
      this.error = null;
      try {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        
        // Update profile with display name
        await updateProfile(userCredential.user, { displayName: name });

        // User document created in PostgreSQL by useFirebaseAuth composable (onAuthStateChanged)
        this.user = {
          uid: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: name,
          photoURL: userCredential.user.photoURL,
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
      
      // Mark survey completed via PostgreSQL backend (if needed in future)
      // For now just update local state
      this.user.surveyCompleted = true;
    },
  },
});
