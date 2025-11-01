import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5001/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// API methods
export const apiService = {
  // Health check
  healthCheck: () => api.get('/health'),

  // File upload
  uploadDocument: (file, userId) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('userId', userId);
    return api.post('/upload/document', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },

  // URL upload
  uploadURL: (url, userId) => api.post('/upload/url', { url, userId }),

  // Text simplification
  simplifyText: (text, level = 'simple') =>
    api.post('/accessibility/simplify-text', { text, level }),

  // Text-to-speech
  textToSpeech: (text, voice = 'en-US-Standard-A', speed = 1.0) =>
    api.post('/accessibility/text-to-speech', { text, voice, speed }),

  // Get available TTS voices
  getVoices: () => api.get('/accessibility/available-voices'),

  // Image description
  imageDescription: (imageFile) => {
    const formData = new FormData();
    formData.append('image', imageFile);
    return api.post('/accessibility/image-description', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },

  // Math to speech
  mathToSpeech: (mathExpression) =>
    api.post('/accessibility/math-to-speech', { mathExpression }),

  // Process document
  processDocument: (fileId, options) =>
    api.post('/process/document', { fileId, options }),

  // Process URL
  processURL: (url, userId) => api.post('/process/url', { url, userId }),

  // User profile
  getUserProfile: (userId) => api.get(`/user/profile/${userId}`),

  // Update preferences
  updatePreferences: (userId, preferences) =>
    api.put('/user/preferences', { userId, preferences }),

  // Submit survey
  submitSurvey: (userId, responses, rating) =>
    api.post('/survey/submit', { userId, responses, rating }),
};

export default api;
