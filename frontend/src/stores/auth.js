import { defineStore } from 'pinia';
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  updateProfile,
} from 'firebase/auth';
import { auth, db } from '../config/firebase';
import { doc, setDoc, getDoc } from 'firebase/firestore';

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
            // Get additional user data from Firestore
            const userDoc = await getDoc(doc(db, 'users', user.uid));
            this.user = {
              uid: user.uid,
              email: user.email,
              displayName: user.displayName,
              photoURL: user.photoURL,
              ...userDoc.data(),
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
        const userDoc = await getDoc(doc(db, 'users', userCredential.user.uid));
        this.user = {
          uid: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: userCredential.user.displayName,
          photoURL: userCredential.user.photoURL,
          ...userDoc.data(),
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

        // Create user document in Firestore
        await setDoc(doc(db, 'users', userCredential.user.uid), {
          email,
          displayName: name,
          createdAt: new Date().toISOString(),
          preferences: {
            theme: 'light',
            fontSize: 'medium',
            dyslexiaFont: false,
            highContrast: false,
            textToSpeech: false,
          },
          surveyCompleted: false,
        });

        this.user = {
          uid: userCredential.user.uid,
          email: userCredential.user.email,
          displayName: name,
          preferences: {
            theme: 'light',
            fontSize: 'medium',
            dyslexiaFont: false,
            highContrast: false,
            textToSpeech: false,
          },
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

      try {
        await setDoc(
          doc(db, 'users', this.user.uid),
          { preferences },
          { merge: true }
        );
        this.user.preferences = { ...this.user.preferences, ...preferences };
        return { success: true };
      } catch (error) {
        return { success: false, error: error.message };
      }
    },

    async markSurveyCompleted() {
      if (!this.user) return;
      
      try {
        await setDoc(
          doc(db, 'users', this.user.uid),
          { surveyCompleted: true },
          { merge: true }
        );
        this.user.surveyCompleted = true;
      } catch (error) {
        console.error('Error marking survey completed:', error);
      }
    },
  },
});
