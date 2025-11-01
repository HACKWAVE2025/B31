# Accessibility Learning Hub - Backend API

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A comprehensive Flask backend API for the Accessibility Learning Hub platform, providing advanced accessibility features for educational content transformation.

## 🌟 Features

### Core Capabilities
- ✅ **Document Processing**: PDF, DOCX, TXT, and image file parsing
- ✅ **URL Content Extraction**: Extract and process content from web articles
- ✅ **Text Simplification**: AI-powered text simplification for cognitive accessibility
- ✅ **Text-to-Speech**: Multiple TTS providers (Google Cloud, Amazon Polly, gTTS)
- ✅ **Image Accessibility**: Automatic ALT text generation and diagram descriptions
- ✅ **Math Processing**: LaTeX equation conversion to accessible formats
- ✅ **Dyslexia Support**: Font and formatting recommendations
- ✅ **Color Contrast Checking**: WCAG compliance verification
- ✅ **User Profiles**: Personalized preferences and accessibility settings
- ✅ **Survey System**: Adaptive recommendations based on user needs
- ✅ **Firebase Integration**: Authentication and database management

### Accessibility Features
- 📖 Text simplification (adjustable grade levels)
- 🔊 Multi-provider text-to-speech
- 🎨 Dyslexia-friendly formatting
- 🖼️ Automatic image ALT text generation
- 📊 Diagram and flowchart descriptions
- 🧮 Mathematical equation narration
- 🎯 Key points extraction
- 📐 Document structure analysis
- 🌈 Color contrast verification

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Firebase account (for authentication)
- Google Cloud account (optional, for advanced features)
- AWS account (optional, for Amazon Polly)

### Installation

#### Automated Setup (Recommended)

**On macOS/Linux:**
```bash
cd backend
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```bash
cd backend
setup.bat
```

#### Manual Setup

1. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download NLP models**
```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your credentials
```

5. **Set up Firebase**
- Download Firebase Admin SDK credentials
- Place JSON file in backend directory
- Update `FIREBASE_CREDENTIALS_PATH` in `.env`

6. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📁 Project Structure

```
backend/
├── app.py                          # Main application entry point
├── config.py                       # Configuration management
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
│
├── routes/                         # API route handlers
│   ├── auth.py                     # Authentication endpoints
│   ├── upload.py                   # File upload endpoints
│   ├── processing.py               # Document processing endpoints
│   ├── accessibility.py            # Accessibility features endpoints
│   ├── user.py                     # User management endpoints
│   └── survey.py                   # Survey and recommendations
│
├── services/                       # Business logic services
│   ├── firebase_service.py         # Firebase integration
│   ├── document_processor.py       # Document parsing
│   ├── url_processor.py            # URL content extraction
│   ├── tts_service.py              # Text-to-speech services
│   ├── accessibility_service.py    # Accessibility transformations
│   └── image_accessibility_service.py # Image processing
│
├── uploads/                        # User uploaded files
├── generated/                      # Generated content (audio, etc.)
├── temp/                           # Temporary files
│
├── API_DOCUMENTATION.md            # Comprehensive API docs
├── FRONTEND_INTEGRATION.md         # Frontend integration guide
├── README.md                       # This file
├── setup.sh                        # Setup script (Unix)
└── setup.bat                       # Setup script (Windows)
```

## 🔑 Environment Configuration

Required environment variables (see `.env.example`):

### Flask Configuration
```bash
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
PORT=5000
```

### Firebase Configuration
```bash
FIREBASE_CREDENTIALS_PATH=path/to/firebase-credentials.json
FIREBASE_API_KEY=your-api-key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
```

### Google Cloud (Optional)
```bash
GOOGLE_APPLICATION_CREDENTIALS=path/to/google-credentials.json
GOOGLE_CLOUD_PROJECT_ID=your-project-id
```

### AWS Configuration (Optional)
```bash
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
```

## 📖 API Documentation

Complete API documentation is available in [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

### Quick API Reference

#### Health Check
```bash
GET /api/health
```

#### Upload File
```bash
POST /api/upload/file
Content-Type: multipart/form-data
Authorization: Bearer <token>

Form Data:
- file: <file>
```

#### Simplify Text
```bash
POST /api/accessibility/simplify-text
Authorization: Bearer <token>

{
  "text": "Complex text here",
  "target_grade_level": 8
}
```

#### Text-to-Speech
```bash
POST /api/accessibility/text-to-speech
Authorization: Bearer <token>

{
  "text": "Text to convert",
  "provider": "gtts",
  "language": "en-US"
}
```

#### Full Transformation
```bash
POST /api/accessibility/full-transformation
Authorization: Bearer <token>

{
  "text": "Document text",
  "adaptations": ["simplify", "dyslexia", "tts", "key_points"],
  "tts_provider": "gtts",
  "simplify_grade": 8
}
```

## 🎯 Use Cases

### 1. Academic Paper Processing
```python
# Upload paper
# Extract text
# Simplify to grade 8 level
# Generate TTS audio
# Extract key points
# Describe mathematical equations
```

### 2. Technical Documentation
```python
# Process PDF documentation
# Generate dyslexia-friendly version
# Create diagram descriptions
# Add image ALT text
# Generate audio narration
```

### 3. Web Article Accessibility
```python
# Extract content from URL
# Simplify language
# Check color contrast
# Generate accessible version
# Save for offline access
```

## 🔧 Advanced Configuration

### Custom TTS Voices

#### Google Cloud TTS
```python
{
  "provider": "google",
  "voice": "en-US-Neural2-C",
  "language": "en-US",
  "speaking_rate": 1.0
}
```

#### Amazon Polly
```python
{
  "provider": "polly",
  "voice_id": "Joanna",
  "language_code": "en-US",
  "engine": "neural"
}
```

### Simplification Levels
- Elementary: Grade 3-5
- Middle School: Grade 6-8
- High School: Grade 9-12
- College: Grade 12+

### Supported File Types
- Documents: PDF, DOCX, DOC, TXT
- Images: PNG, JPG, JPEG, GIF
- Web: Any valid URL

## 🧪 Testing

### Test API Health
```bash
curl http://localhost:5000/api/health
```

### Test with Sample Data
```bash
# Simplify text
curl -X POST http://localhost:5000/api/accessibility/simplify-text \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is a complex sentence with sophisticated vocabulary.", "target_grade_level": 6}'
```

## 🌐 Frontend Integration

Complete frontend integration guide available in [FRONTEND_INTEGRATION.md](./FRONTEND_INTEGRATION.md)

### Quick Integration (Vue.js/React)
```javascript
import { api } from './services/api';

// Upload file
const formData = new FormData();
formData.append('file', file);
const response = await api.upload.file(formData);

// Process document
const result = await api.accessibility.fullTransformation(
  extractedText,
  ['simplify', 'tts', 'dyslexia']
);
```

## 🔒 Security

- Firebase authentication required for all user endpoints
- File upload size limited to 50MB
- Input validation on all endpoints
- Secure file storage with user isolation
- CORS configuration for frontend access

## 🚦 Rate Limiting (Recommended for Production)

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get('Authorization'),
    default_limits=["200 per day", "50 per hour"]
)
```

## 📊 Monitoring

### Health Check Endpoint
```bash
GET /api/health
```

Returns:
```json
{
  "status": "healthy",
  "service": "Accessibility Learning Hub API",
  "version": "1.0.0"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👥 Authors

Built for the Accessibility Learning Hub project

## 🙏 Acknowledgments

- Firebase for authentication and database
- Google Cloud for Vision and TTS APIs
- Amazon Web Services for Polly TTS
- spaCy for NLP processing
- All open-source contributors

## 📞 Support

For issues and questions:
- Check API documentation
- Review integration guide
- Contact development team

## 🗺️ Roadmap

- [ ] Add support for more document formats (PPTX, ODT)
- [ ] Implement real-time collaboration features
- [ ] Add support for more languages
- [ ] Enhanced diagram recognition
- [ ] Video content accessibility
- [ ] Mobile app API endpoints
- [ ] Advanced analytics dashboard

---

**Happy Coding! 🚀**

Made with ❤️ for accessibility
