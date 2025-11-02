import { defineStore } from 'pinia';
import databaseService from '../services/database.service';

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
    // processedContent is the same as savedContent
    // (when you save processed content, it means it's been processed)
  },

  actions: {
    /**
     * Fetch all user content from PostgreSQL database
     */
    async fetchUserContent(userId) {
      this.loading = true;
      this.error = null;
      try {
        // Fetch uploads from database
        const uploads = await databaseService.getUserUploads(userId);
        this.uploads = uploads;

        // Fetch saved content from database
        const savedContent = await databaseService.getSavedContent(userId);
        this.savedContent = savedContent;
        
        // processedContent is the same as savedContent
        // (savedContent means the file was processed and saved)
        this.processedContent = savedContent;

        return { success: true };
      } catch (error) {
        this.error = error.message;
        console.error('Fetch user content error:', error);
        return { success: false, error: error.message };
      } finally {
        this.loading = false;
      }
    },

    /**
     * Save upload to PostgreSQL database
     */
    async saveUpload(userId, uploadData) {
      try {
        const saved = await databaseService.saveUpload({
          userId,
          ...uploadData,
        });
        
        this.uploads.unshift(saved);
        return { success: true, data: saved };
      } catch (error) {
        console.error('Save upload error:', error);
        return { success: false, error: error.message };
      }
    },

    /**
     * Save processed content to PostgreSQL database
     */
    async saveProcessedContent(userId, contentData) {
      try {
        const saved = await databaseService.saveContent({
          userId,
          ...contentData,
        });
        
        this.savedContent.unshift(saved);
        // Also add to processedContent since they're the same
        this.processedContent.unshift(saved);
        return { success: true, data: saved };
      } catch (error) {
        console.error('Save content error:', error);
        return { success: false, error: error.message };
      }
    },

    /**
     * Delete saved content from PostgreSQL database
     */
    async deleteContent(contentId) {
      try {
        await databaseService.deleteSavedContent(contentId);
        this.savedContent = this.savedContent.filter((c) => c.id !== contentId);
        this.processedContent = this.processedContent.filter((c) => c.id !== contentId);
        return { success: true };
      } catch (error) {
        console.error('Delete content error:', error);
        return { success: false, error: error.message };
      }
    },

    /**
     * Delete upload from PostgreSQL database
     */
    async deleteUpload(uploadId) {
      try {
        await databaseService.deleteUpload(uploadId);
        this.uploads = this.uploads.filter((u) => u.id !== uploadId);
        return { success: true };
      } catch (error) {
        console.error('Delete upload error:', error);
        return { success: false, error: error.message };
      }
    },

    /**
     * Get user statistics
     */
    async fetchUserStats(userId) {
      try {
        const stats = await databaseService.getUserStats(userId);
        return { success: true, data: stats };
      } catch (error) {
        console.error('Fetch stats error:', error);
        return { success: false, error: error.message };
      }
    },

    setCurrentContent(content) {
      this.currentContent = content;
    },

    clearCurrentContent() {
      this.currentContent = null;
    },

    // Local storage methods for demo mode (backward compatibility)
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
