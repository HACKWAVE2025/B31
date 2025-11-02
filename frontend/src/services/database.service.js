/**
 * Database API Service - PostgreSQL backend integration
 * Handles all CRUD operations for users, uploads, and saved content
 */

import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001/api';

class DatabaseService {
  constructor() {
    this.api = axios.create({
      baseURL: `${API_BASE_URL}/db`,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  // ==================== USER OPERATIONS ====================

  /**
   * Create or update user in database
   */
  async createUser(userData) {
    try {
      const response = await this.api.post('/users', userData);
      return response.data;
    } catch (error) {
      console.error('Create user error:', error);
      throw error;
    }
  }

  /**
   * Get user by ID
   */
  async getUser(userId) {
    try {
      const response = await this.api.get(`/users/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Get user error:', error);
      throw error;
    }
  }

  // ==================== UPLOAD OPERATIONS ====================

  /**
   * Save upload metadata to database
   */
  async saveUpload(uploadData) {
    try {
      const response = await this.api.post('/uploads', uploadData);
      return response.data;
    } catch (error) {
      console.error('Save upload error:', error);
      throw error;
    }
  }

  /**
   * Get all uploads for a user
   */
  async getUserUploads(userId) {
    try {
      const response = await this.api.get(`/uploads/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Get uploads error:', error);
      throw error;
    }
  }

  /**
   * Delete an upload
   */
  async deleteUpload(uploadId) {
    try {
      const response = await this.api.delete(`/uploads/${uploadId}`);
      return response.data;
    } catch (error) {
      console.error('Delete upload error:', error);
      throw error;
    }
  }

  // ==================== SAVED CONTENT OPERATIONS ====================

  /**
   * Save processed content to database
   */
  async saveContent(contentData) {
    try {
      const response = await this.api.post('/saved-content', contentData);
      return response.data;
    } catch (error) {
      console.error('Save content error:', error);
      throw error;
    }
  }

  /**
   * Get all saved content for a user
   */
  async getSavedContent(userId) {
    try {
      const response = await this.api.get(`/saved-content/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Get saved content error:', error);
      throw error;
    }
  }

  /**
   * Get a specific saved content item
   */
  async getSavedContentItem(contentId) {
    try {
      const response = await this.api.get(`/saved-content/item/${contentId}`);
      return response.data;
    } catch (error) {
      console.error('Get content item error:', error);
      throw error;
    }
  }

  /**
   * Delete saved content
   */
  async deleteSavedContent(contentId) {
    try {
      const response = await this.api.delete(`/saved-content/${contentId}`);
      return response.data;
    } catch (error) {
      console.error('Delete saved content error:', error);
      throw error;
    }
  }

  // ==================== USER PREFERENCES OPERATIONS ====================

  /**
   * Get user preferences
   */
  async getPreferences(userId) {
    try {
      const response = await this.api.get(`/preferences/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Get preferences error:', error);
      throw error;
    }
  }

  /**
   * Update user preferences
   */
  async updatePreferences(userId, preferences) {
    try {
      const response = await this.api.put(`/preferences/${userId}`, preferences);
      return response.data;
    } catch (error) {
      console.error('Update preferences error:', error);
      throw error;
    }
  }

  /**
   * Update user survey data
   */
  async updateUserSurvey(userId, surveyData) {
    try {
      const response = await this.api.put(`/users/${userId}/survey`, surveyData);
      return response.data;
    } catch (error) {
      console.error('Update survey error:', error);
      throw error;
    }
  }

  // ==================== STATS OPERATIONS ====================

  /**
   * Get user statistics (uploads, saved content, recent activity)
   */
  async getUserStats(userId) {
    try {
      const response = await this.api.get(`/stats/${userId}`);
      return response.data;
    } catch (error) {
      console.error('Get stats error:', error);
      throw error;
    }
  }
}

export default new DatabaseService();
