import { defineStore } from 'pinia';
import { db } from '../config/firebase';
import {
  collection,
  addDoc,
  getDocs,
  doc,
  updateDoc,
  deleteDoc,
  query,
  where,
  orderBy,
  limit as firestoreLimit,
} from 'firebase/firestore';

export const useContentStore = defineStore('content', {
  state: () => ({
    uploads: [],
    processedContent: [],
    savedContent: [],
    history: [],
    currentContent: null,
    loading: false,
    error: null,
  }),

  getters: {
    recentUploads: (state) => state.uploads.slice(0, 5),
    recentProcessed: (state) => state.processedContent.slice(0, 5),
  },

  actions: {
    async fetchUserContent(userId) {
      this.loading = true;
      this.error = null;
      try {
        // Fetch uploads
        const uploadsRef = collection(db, 'uploads');
        const uploadsQuery = query(
          uploadsRef,
          where('userId', '==', userId),
          orderBy('createdAt', 'desc')
        );
        const uploadsSnapshot = await getDocs(uploadsQuery);
        this.uploads = uploadsSnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));

        // Fetch processed content
        const processedRef = collection(db, 'processedContent');
        const processedQuery = query(
          processedRef,
          where('userId', '==', userId),
          orderBy('createdAt', 'desc')
        );
        const processedSnapshot = await getDocs(processedQuery);
        this.processedContent = processedSnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));

        // Fetch saved content
        const savedRef = collection(db, 'savedContent');
        const savedQuery = query(
          savedRef,
          where('userId', '==', userId),
          orderBy('savedAt', 'desc')
        );
        const savedSnapshot = await getDocs(savedQuery);
        this.savedContent = savedSnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));

        return { success: true };
      } catch (error) {
        this.error = error.message;
        return { success: false, error: error.message };
      } finally {
        this.loading = false;
      }
    },

    async saveUpload(userId, file, metadata) {
      try {
        const uploadData = {
          userId,
          fileName: file.name,
          fileType: file.type,
          fileSize: file.size,
          metadata: metadata || {},
          createdAt: new Date().toISOString(),
          status: 'uploaded',
        };

        const docRef = await addDoc(collection(db, 'uploads'), uploadData);
        this.uploads.unshift({ id: docRef.id, ...uploadData });
        return { success: true, id: docRef.id };
      } catch (error) {
        return { success: false, error: error.message };
      }
    },

    async saveProcessedContent(userId, content) {
      try {
        const contentData = {
          userId,
          ...content,
          createdAt: new Date().toISOString(),
        };

        const docRef = await addDoc(collection(db, 'processedContent'), contentData);
        this.processedContent.unshift({ id: docRef.id, ...contentData });
        return { success: true, id: docRef.id };
      } catch (error) {
        return { success: false, error: error.message };
      }
    },

    async saveContent(userId, contentId, contentData) {
      try {
        const saveData = {
          userId,
          contentId,
          ...contentData,
          savedAt: new Date().toISOString(),
        };

        const docRef = await addDoc(collection(db, 'savedContent'), saveData);
        this.savedContent.unshift({ id: docRef.id, ...saveData });
        return { success: true, id: docRef.id };
      } catch (error) {
        return { success: false, error: error.message };
      }
    },

    async deleteContent(contentId, type = 'saved') {
      try {
        const collectionName =
          type === 'saved' ? 'savedContent' : type === 'processed' ? 'processedContent' : 'uploads';
        await deleteDoc(doc(db, collectionName, contentId));

        // Remove from state
        if (type === 'saved') {
          this.savedContent = this.savedContent.filter((c) => c.id !== contentId);
        } else if (type === 'processed') {
          this.processedContent = this.processedContent.filter((c) => c.id !== contentId);
        } else {
          this.uploads = this.uploads.filter((c) => c.id !== contentId);
        }

        return { success: true };
      } catch (error) {
        return { success: false, error: error.message };
      }
    },

    setCurrentContent(content) {
      this.currentContent = content;
    },

    clearCurrentContent() {
      this.currentContent = null;
    },

    // Local storage methods for demo mode (no Firebase)
    addUpload(upload) {
      this.uploads.unshift(upload);
    },

    addSavedContent(content) {
      this.savedContent.unshift(content);
    },

    removeSavedContent(id) {
      this.savedContent = this.savedContent.filter(c => c.id !== id);
    },
  },
});
