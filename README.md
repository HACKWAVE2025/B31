<div align="center">

# 🚀 SkillSet AI

### *Unlock Your Potential with AI-Powered Learning*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Vue 3](https://img.shields.io/badge/Vue-3.5.22-4FC08D?logo=vue.js&logoColor=white)](https://vuejs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-8E75B2?logo=google&logoColor=white)](https://ai.google.dev/)

</div>

---

## ✨ **What is SkillSet AI?**

**SkillSet AI** is an intelligent learning platform that transforms how you discover, develop, and master new skills. Powered by **Google Gemini 2.0 Flash**, our platform analyzes your strengths, identifies skill gaps, and creates personalized learning roadmaps tailored to your career goals.

### 🎯 **Key Features**

<table>
<tr>
<td width="50%">

#### 🧠 **AI Skill Assessment**
Get comprehensive AI-powered evaluations of your current skill set with detailed insights and recommendations.

#### 📚 **Smart Learning Paths**
Receive curated resources and personalized roadmaps based on your unique learning style and goals.

</td>
<td width="50%">

#### 📊 **Progress Analytics**
Track your improvement with detailed metrics, visualizations, and performance insights.

#### 🎯 **Gap Detection**
Identify exactly where you need to improve with intelligent skill gap analysis.

</td>
</tr>
</table>

---

## 🎨 **Stunning UI/UX**

Experience a **visually breathtaking** landing page with cutting-edge animations:

- **🌊 DitherBackground** - Three.js dithered wave effects with mouse interaction (dark mode)
- **🌈 Iridescence** - WebGL rainbow gradient animations (light mode)
- **🎯 DecryptedText** - Matrix-style text scrambling on "SKILLSET AI" title
- **💫 BlurText** - Smooth blur-in reveals for all headings
- **🎪 BounceCards** - GSAP-powered elastic physics animations
- **🎭 Theme Toggle** - Seamless dark/light mode transitions
- **🖱️ Mouse Reactive** - Backgrounds that respond to cursor movement

---

## 🛠️ **Tech Stack**

### **Frontend**
```
Vue 3.5.22 (Composition API) + Vite 7.1.12
Three.js 0.158.0 + Post-processing
GSAP 3.13.0 + @vueuse/motion
Firebase Auth 12.5.0
TailwindCSS + Pinia
```

### **Backend**
```
Flask 3.1.2 + Python 3.12
SQLAlchemy 2.0.44 + PostgreSQL 15
Google Gemini 2.0 Flash Exp
PyPDF2 + BeautifulSoup4
CORS + JWT Authentication
```

### **Database**
```sql
PostgreSQL 15 with 4 tables:
├── users (Firebase Auth sync)
├── uploads (document processing)
├── saved_content (AI-simplified content)
└── user_preferences (personalization)
```

---

## 🚀 **Quick Start**

### **Prerequisites**
- Node.js 18+ & npm
- Python 3.12+
- PostgreSQL 15
- Firebase Account
- Google Gemini API Key

### **1. Clone the Repository**
```bash
git clone https://github.com/HACKWAVE2025/B31.git
cd B31
```

### **2. Backend Setup**
```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials:
# - DATABASE_URL
# - GEMINI_API_KEY
# - FIREBASE_CREDENTIALS (optional)

# Create PostgreSQL database
createdb skillsetai_db

# Run the server
python app.py
```

**Backend will run on:** `http://127.0.0.1:5001`

### **3. Frontend Setup**
```bash
cd frontend

# Install dependencies
npm install

# Set up Firebase config
# Edit src/config/firebase.js with your Firebase credentials

# Run development server
npm run dev
```

**Frontend will run on:** `http://localhost:5173`

---

## 📁 **Project Structure**

```
skillsetai/
├── 📂 backend/
│   ├── app.py                    # Flask application factory
│   ├── config.py                 # Configuration management
│   ├── requirements.txt          # Python dependencies
│   ├── 📂 routes/                # API endpoints
│   │   ├── auth.py              # Authentication routes
│   │   ├── upload.py            # File upload handling
│   │   ├── processing.py        # AI processing routes
│   │   ├── survey.py            # Skill assessment
│   │   └── user.py              # User management
│   └── 📂 services/             # Business logic
│       ├── document_processor.py # PDF/URL extraction
│       ├── firebase_service.py   # Firebase integration
│       └── accessibility_service.py # AI simplification
│
├── 📂 frontend/
│   ├── 📂 src/
│   │   ├── 📂 views/            # Page components
│   │   │   ├── HomePage.vue     # Landing page
│   │   │   └── DashboardHome.vue
│   │   ├── 📂 components/       # Reusable components
│   │   │   ├── DitherBackground.vue  # Three.js waves
│   │   │   ├── Iridescence.vue       # Rainbow gradient
│   │   │   ├── DecryptedText.vue     # Text scrambling
│   │   │   ├── BlurText.vue          # Blur animations
│   │   │   ├── BounceCards.vue       # Elastic cards
│   │   │   ├── AdvancedGrid.vue      # Feature grid
│   │   │   ├── TestimonialsCarousel.vue
│   │   │   └── CTABand.vue           # Call-to-action
│   │   ├── 📂 composables/      # Vue composables
│   │   │   └── useFirebaseAuth.js
│   │   ├── 📂 stores/           # Pinia state management
│   │   └── 📂 router/           # Vue Router
│   └── package.json
│
└── README.md
```

---

## 🎬 **Features in Action**

### **🔐 Authentication**
- Firebase Email/Password Authentication
- Google OAuth Sign-In
- PostgreSQL User Sync
- JWT Token Management
- Protected Dashboard Routes

### **📤 Document Processing**
- PDF Text Extraction (PyPDF2)
- URL Content Scraping (BeautifulSoup4)
- AI-Powered Simplification (Gemini 2.0)
- Multi-format Support
- Cloud Storage Integration

### **🤖 AI-Powered Features**
- Skill Gap Analysis
- Personalized Recommendations
- Content Simplification
- Reading Level Adjustment
- Learning Path Generation

### **♿ Accessibility**
- Text-to-Speech Support
- Dyslexia-friendly Fonts
- High Contrast Mode
- Image Descriptions
- Customizable Reading Levels

---

## 🌟 **Landing Page Components**

Our landing page features **9 custom-built animated components**:

| Component | Description | Technology |
|-----------|-------------|------------|
| 🌊 **DitherBackground** | Dithered wave effects with mouse interaction | Three.js + Post-processing |
| 🌈 **Iridescence** | Rainbow gradient WebGL animations | Canvas API + WebGL |
| 🎯 **DecryptedText** | Matrix-style character scrambling | Vue 3 Composition API |
| 💫 **BlurText** | Smooth blur-in text reveals | @vueuse/motion |
| 🎪 **BounceCards** | Physics-based elastic cards | GSAP + Elastic easing |
| ⚡ **AdvancedGrid** | 5-card feature showcase | GSAP |
| 💬 **TestimonialsCarousel** | Auto-rotating testimonials | Vue Transitions |
| 🚀 **CTABand** | Aurora glow call-to-action | CSS Animations |
| 🔐 **AuthModal** | Glassmorphic sign-in modal | Vue 3 + Teleport |

---

## 📊 **API Endpoints**

### **Authentication**
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/verify` - Token verification

### **Document Processing**
- `POST /api/upload/document` - Upload PDF/document
- `POST /api/upload/url` - Process URL content
- `GET /api/db/uploads/:userId` - Get user uploads

### **AI Processing**
- `POST /api/process/simplify` - Simplify text
- `POST /api/process/summarize` - Generate summary
- `POST /api/process/analyze` - Skill analysis

### **User Management**
- `GET /api/db/users/:id` - Get user profile
- `POST /api/db/users` - Create/update user
- `GET /api/db/user-preferences/:userId` - Get preferences

---

## 🎨 **Color Palette**

### **Dark Mode**
```css
Background: #000000
Text: #ffffff
Glass: rgba(255, 255, 255, 0.05)
Border: rgba(255, 255, 255, 0.1)
```

### **Light Mode**
```css
Background: #ffffff
Text: #000000
Glass: rgba(255, 255, 255, 0.5)
Border: rgba(0, 0, 0, 0.15)
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📝 **Environment Variables**

### **Backend (.env)**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/skillsetai_db
GEMINI_API_KEY=your_gemini_api_key
FIREBASE_CREDENTIALS=path/to/serviceAccountKey.json (optional)
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

### **Frontend (src/config/firebase.js)**
```javascript
const firebaseConfig = {
  apiKey: "your_api_key",
  authDomain: "your_app.firebaseapp.com",
  projectId: "your_project_id",
  // ... other Firebase config
}
```

---

## 🐛 **Known Issues & Solutions**

### **Issue: White screen on frontend**
- **Solution**: Check browser console for Firebase errors
- Ensure Firebase config is correct
- Verify CORS settings in backend

### **Issue: Backend not connecting to PostgreSQL**
- **Solution**: Create PostgreSQL superuser: `createuser -s postgres`
- Verify DATABASE_URL in .env
- Check PostgreSQL service is running

### **Issue: Animations not loading**
- **Solution**: Clear browser cache
- Run `npm install` to ensure all dependencies are installed
- Check for console errors

---

## 📜 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 **Team**

Built with ❤️ for **HACKWAVE 2025**

- **Team ID**: B31
- **Repository**: [HACKWAVE2025/B31](https://github.com/HACKWAVE2025/B31)

---

## 🙏 **Acknowledgments**

- **Google Gemini AI** for powerful language processing
- **Firebase** for seamless authentication
- **Three.js** for stunning 3D graphics
- **GSAP** for smooth animations
- **Vue.js** community for excellent tooling

---

<div align="center">

### **⭐ Star this repo if you find it helpful!**

Made with 💜 by Team B31

</div>
