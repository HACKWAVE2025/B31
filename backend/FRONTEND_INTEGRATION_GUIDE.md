# Frontend Integration Guide - Accessibility Learning Hub Backend

## 📋 Overview

This guide will help your frontend developer integrate with the Accessibility Learning Hub Backend API. The backend provides document processing, accessibility features, text-to-speech, and more.

---

## 🚀 Quick Start

### Backend Server Information

- **Base URL (Local):** `http://localhost:5001`
- **Base URL (Network):** `http://192.168.182.8:5001`
- **API Prefix:** `/api`
- **CORS Enabled:** Yes (configured for `http://localhost:3000` and `http://localhost:8080`)

### Health Check

Test if the backend is running:
```bash
curl http://localhost:5001/api/health
```

Expected Response:
```json
{
  "status": "healthy",
  "service": "Accessibility Learning Hub API",
  "version": "1.0.0"
}
```

---

## 🔌 API Endpoints

### 1. Authentication (`/api/auth`)

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

---

### 2. File Upload (`/api/upload`)

#### Upload Document
```http
POST /api/upload/document
Content-Type: multipart/form-data

FormData:
  - file: [PDF/DOCX/TXT file]
  - userId: "user123"
```

**Supported File Types:**
- PDF (`.pdf`)
- Word Documents (`.docx`, `.doc`)
- Text Files (`.txt`)
- PowerPoint (`.pptx`)
- Images (`.png`, `.jpg`, `.jpeg`, `.gif`)

**File Size Limit:** 50MB

**Response:**
```json
{
  "success": true,
  "fileId": "abc123",
  "filename": "document.pdf",
  "fileType": "pdf",
  "size": 1024000
}
```

#### Upload URL
```http
POST /api/upload/url
Content-Type: application/json

{
  "url": "https://example.com/article",
  "userId": "user123"
}
```

---

### 3. Document Processing (`/api/process`)

#### Process Document
```http
POST /api/process/document
Content-Type: application/json

{
  "fileId": "abc123",
  "options": {
    "extractText": true,
    "generateSummary": true,
    "simplifyText": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "text": "Extracted text content...",
  "summary": "Brief summary of the document...",
  "simplifiedText": "Easier to read version...",
  "wordCount": 1500,
  "readingLevel": "Grade 8"
}
```

#### Process URL Content
```http
POST /api/process/url
Content-Type: application/json

{
  "url": "https://example.com/article",
  "userId": "user123"
}
```

---

### 4. Accessibility Features (`/api/accessibility`)

#### Text Simplification
```http
POST /api/accessibility/simplify-text
Content-Type: application/json

{
  "text": "The mitochondria is the powerhouse of the cell that produces energy through cellular respiration.",
  "level": "simple"
}
```

**Simplification Levels:**
- `simple` - Basic simplification
- `very_simple` - Maximum simplification
- `medium` - Moderate simplification

**Response:**
```json
{
  "originalText": "The mitochondria is...",
  "simplifiedText": "The cell's power center makes energy.",
  "readabilityScore": {
    "original": 12.5,
    "simplified": 6.2
  }
}
```

#### Text-to-Speech Conversion
```http
POST /api/accessibility/text-to-speech
Content-Type: application/json

{
  "text": "Hello, welcome to our application",
  "voice": "en-US-Standard-A",
  "speed": 1.0
}
```

**Response:**
```json
{
  "success": true,
  "audioUrl": "/generated/audio_abc123.mp3",
  "duration": 3.5,
  "format": "mp3"
}
```

#### Get Available TTS Voices
```http
GET /api/accessibility/available-voices
```

**Response:**
```json
{
  "voices": [
    {
      "id": "en-US-Standard-A",
      "name": "English (US) - Female",
      "language": "en-US",
      "gender": "FEMALE"
    },
    {
      "id": "en-US-Standard-B",
      "name": "English (US) - Male",
      "language": "en-US",
      "gender": "MALE"
    }
  ]
}
```

#### Image Accessibility (Alt Text Generation)
```http
POST /api/accessibility/image-description
Content-Type: multipart/form-data

FormData:
  - image: [image file]
```

**Response:**
```json
{
  "success": true,
  "description": "A photo of a sunset over mountains",
  "labels": ["sunset", "mountains", "nature"],
  "safeSearch": {
    "adult": "VERY_UNLIKELY",
    "violence": "VERY_UNLIKELY"
  }
}
```

#### Math Accessibility
```http
POST /api/accessibility/math-to-speech
Content-Type: application/json

{
  "mathExpression": "x^2 + 5x + 6 = 0"
}
```

**Response:**
```json
{
  "expression": "x^2 + 5x + 6 = 0",
  "spokenForm": "x squared plus 5x plus 6 equals zero",
  "audioUrl": "/generated/math_audio_xyz.mp3"
}
```

---

### 5. User Management (`/api/user`)

#### Get User Profile
```http
GET /api/user/profile/:userId
Authorization: Bearer <token>
```

#### Update User Preferences
```http
PUT /api/user/preferences
Content-Type: application/json
Authorization: Bearer <token>

{
  "userId": "user123",
  "preferences": {
    "defaultVoice": "en-US-Standard-A",
    "textSize": "large",
    "readingSpeed": 1.0,
    "simplificationLevel": "simple"
  }
}
```

---

### 6. Survey/Feedback (`/api/survey`)

#### Submit Survey Response
```http
POST /api/survey/submit
Content-Type: application/json

{
  "userId": "user123",
  "responses": {
    "question1": "Very helpful",
    "question2": "Easy to use"
  },
  "rating": 5
}
```

---

## 🔐 Authentication

### Using Bearer Tokens

After login, include the JWT token in requests:

```javascript
fetch('http://localhost:5001/api/user/profile/user123', {
  headers: {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
    'Content-Type': 'application/json'
  }
})
```

---

## 💻 Frontend Integration Examples

### JavaScript (Fetch API)

#### Example 1: Simplify Text
```javascript
async function simplifyText(text) {
  try {
    const response = await fetch('http://localhost:5001/api/accessibility/simplify-text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text: text,
        level: 'simple'
      })
    });
    
    const data = await response.json();
    return data.simplifiedText;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}
```

#### Example 2: Upload File
```javascript
async function uploadDocument(file, userId) {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('userId', userId);
  
  try {
    const response = await fetch('http://localhost:5001/api/upload/document', {
      method: 'POST',
      body: formData
    });
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error uploading file:', error);
    throw error;
  }
}
```

#### Example 3: Text-to-Speech
```javascript
async function convertTextToSpeech(text, voice = 'en-US-Standard-A') {
  try {
    const response = await fetch('http://localhost:5001/api/accessibility/text-to-speech', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text: text,
        voice: voice,
        speed: 1.0
      })
    });
    
    const data = await response.json();
    // Return the audio URL to play in frontend
    return `http://localhost:5001${data.audioUrl}`;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}
```

### React Example

```jsx
import React, { useState } from 'react';

function TextSimplifier() {
  const [inputText, setInputText] = useState('');
  const [simplifiedText, setSimplifiedText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSimplify = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5001/api/accessibility/simplify-text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: inputText,
          level: 'simple'
        })
      });
      
      const data = await response.json();
      setSimplifiedText(data.simplifiedText);
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to simplify text');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to simplify..."
      />
      <button onClick={handleSimplify} disabled={loading}>
        {loading ? 'Simplifying...' : 'Simplify Text'}
      </button>
      {simplifiedText && (
        <div>
          <h3>Simplified Text:</h3>
          <p>{simplifiedText}</p>
        </div>
      )}
    </div>
  );
}

export default TextSimplifier;
```

### Vue.js Example

```vue
<template>
  <div>
    <textarea 
      v-model="inputText" 
      placeholder="Enter text to simplify..."
    ></textarea>
    <button @click="simplifyText" :disabled="loading">
      {{ loading ? 'Simplifying...' : 'Simplify Text' }}
    </button>
    <div v-if="simplifiedText">
      <h3>Simplified Text:</h3>
      <p>{{ simplifiedText }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
      simplifiedText: '',
      loading: false
    }
  },
  methods: {
    async simplifyText() {
      this.loading = true;
      try {
        const response = await fetch('http://localhost:5001/api/accessibility/simplify-text', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            text: this.inputText,
            level: 'simple'
          })
        });
        
        const data = await response.json();
        this.simplifiedText = data.simplifiedText;
      } catch (error) {
        console.error('Error:', error);
        alert('Failed to simplify text');
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>
```

### Axios Example

```javascript
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5001/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add token to requests
api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// API functions
export const simplifyText = async (text, level = 'simple') => {
  const response = await api.post('/accessibility/simplify-text', {
    text,
    level
  });
  return response.data;
};

export const uploadDocument = async (file, userId) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('userId', userId);
  
  const response = await api.post('/upload/document', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
  return response.data;
};

export const textToSpeech = async (text, voice = 'en-US-Standard-A') => {
  const response = await api.post('/accessibility/text-to-speech', {
    text,
    voice,
    speed: 1.0
  });
  return response.data;
};
```

---

## 🛠️ Running the Backend Locally

### Prerequisites
- Python 3.12 installed
- Virtual environment set up

### Start the Server

```bash
cd /Users/jaideepamrabad/Documents/skillsetai/backend
./venv/bin/python3 app.py
```

Or use the full path:
```bash
PYTHONPATH=/Users/jaideepamrabad/Documents/skillsetai/backend \
/Users/jaideepamrabad/Documents/skillsetai/backend/venv/bin/python3 \
/Users/jaideepamrabad/Documents/skillsetai/backend/app.py
```

**Server will start on:** `http://localhost:5001`

---

## 🌐 CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:3000` (React default)
- `http://localhost:8080` (Vue default)

If your frontend runs on a different port, update the `.env` file:

```bash
CORS_ORIGINS=http://localhost:3000,http://localhost:8080,http://localhost:4200
```

---

## 📝 Environment Variables

Create a `.env` file in the backend directory:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Server Configuration
PORT=5001

# Firebase Configuration (Optional)
FIREBASE_CREDENTIALS_PATH=path/to/credentials.json
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com

# Google Cloud (Optional)
GOOGLE_CLOUD_PROJECT_ID=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# AWS (Optional)
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1

# File Upload Configuration
MAX_CONTENT_LENGTH=52428800
UPLOAD_FOLDER=uploads

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8080
```

---

## 🧪 Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:5001/api/health

# Simplify text
curl -X POST http://localhost:5001/api/accessibility/simplify-text \
  -H "Content-Type: application/json" \
  -d '{"text": "Complex text here", "level": "simple"}'

# Get available voices
curl http://localhost:5001/api/accessibility/available-voices

# Upload file
curl -X POST http://localhost:5001/api/upload/document \
  -F "file=@/path/to/document.pdf" \
  -F "userId=user123"
```

### Using Postman

1. Import the API endpoints
2. Set base URL: `http://localhost:5001`
3. For file uploads, use form-data in Body
4. For JSON requests, set Content-Type header to `application/json`

### Test Script

Run the provided test script:
```bash
cd backend
bash test_api.sh
```

---

## 📊 Response Formats

### Success Response
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### Error Response
```json
{
  "error": "Error message here",
  "code": "ERROR_CODE",
  "status": 400
}
```

### Common HTTP Status Codes
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `413` - File Too Large (> 50MB)
- `500` - Internal Server Error

---

## 🔒 Security Best Practices

1. **Always use HTTPS in production**
2. **Store API tokens securely** (use environment variables, not hardcoded)
3. **Validate file uploads** on frontend before sending
4. **Handle errors gracefully** with try-catch blocks
5. **Implement rate limiting** on frontend to prevent spam
6. **Sanitize user inputs** before sending to API

---

## 🐛 Common Issues & Solutions

### Issue 1: CORS Error
**Problem:** Frontend can't connect to backend
**Solution:** Add your frontend URL to `CORS_ORIGINS` in `.env`

### Issue 2: File Upload Fails
**Problem:** 413 File Too Large error
**Solution:** Check file size (max 50MB) or increase `MAX_CONTENT_LENGTH`

### Issue 3: Connection Refused
**Problem:** Cannot connect to `http://localhost:5001`
**Solution:** Ensure backend server is running. Check with `curl http://localhost:5001/api/health`

### Issue 4: Firebase Warnings
**Problem:** "Firebase credentials not found" warning
**Solution:** This is expected if Firebase is not configured. Basic features work without it.

---

## 📞 Support & Contact

For questions or issues:
1. Check the main README.md
2. Review API documentation in `/backend/API_DOCUMENTATION.md`
3. Check endpoint examples in `/backend/ENDPOINTS_SUMMARY.md`
4. Test with the provided `test_api.sh` script

---

## 🚀 Production Deployment

For production deployment:
1. Set `FLASK_ENV=production` in `.env`
2. Use a production WSGI server (gunicorn included)
3. Set up proper SSL/TLS certificates
4. Configure environment-specific CORS origins
5. Set up proper logging and monitoring

**Run with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

---

## 📚 Additional Resources

- **Full API Documentation:** `/backend/API_DOCUMENTATION.md`
- **Endpoint Summary:** `/backend/ENDPOINTS_SUMMARY.md`
- **Project Overview:** `/backend/PROJECT_OVERVIEW.md`
- **Testing Guide:** `/backend/TESTING_GUIDE.md`
- **Deployment Guide:** `/backend/DEPLOYMENT.md`

---

## ✅ Quick Checklist for Frontend Developer

- [ ] Backend server is running on `http://localhost:5001`
- [ ] Can access health check endpoint
- [ ] CORS is configured for your frontend URL
- [ ] Understand authentication flow (if needed)
- [ ] Know how to upload files
- [ ] Know how to handle API responses
- [ ] Error handling implemented
- [ ] Have `.env` file configured
- [ ] Tested basic endpoints with cURL or Postman

---

**Version:** 1.0.0  
**Last Updated:** November 1, 2025  
**Maintained By:** Accessibility Learning Hub Team
