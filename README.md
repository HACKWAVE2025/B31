# � Accessibility Learning Hub

**Transform educational content into accessible, easy-to-understand formats using AI**

A full-stack web application that makes learning materials accessible to everyone, powered by Google Gemini AI and modern web technologies.

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://python.org)
[![Vue.js](https://img.shields.io/badge/vue-3.5-green.svg)](https://vuejs.org)
[![Flask](https://img.shields.io/badge/flask-3.0-orange.svg)](https://flask.palletsprojects.com)
[![Tailwind](https://img.shields.io/badge/tailwind-3.4-cyan.svg)](https://tailwindcss.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 What This Does

Upload any document (PDF, DOCX, TXT, images) or URL, and get:
- ✨ **AI-Simplified Text** - Rewritten for different reading levels using Gemini AI
- 📝 **Smart Summaries** - Key points extracted automatically
- 🔊 **Text-to-Speech** - Listen instead of read
- 🖼️ **Image Descriptions** - AI-generated accessible image descriptions
- 💾 **Save & Review** - Keep your processed content for later
- 🎨 **Dyslexia-Friendly** - Special fonts and formatting options
- 🌙 **Dark Mode** - Easy on the eyes

---

## 🚀 Quick Start (For Cloning)

### Prerequisites
Before you begin, make sure you have these installed:
- **Python 3.12+** - [Download here](https://python.org)
- **Node.js 18+** - [Download here](https://nodejs.org)
- **Git** - [Download here](https://git-scm.com)

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd skillsetai
```

### 2️⃣ Backend Setup (5 minutes)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Create environment file
touch .env
```

**Configure `.env` file:**
Open `backend/.env` and add:
```env
# Flask Configuration
SECRET_KEY=your-secret-key-change-this-in-production
FLASK_ENV=development
PORT=5001

# Google Gemini AI (REQUIRED)
GEMINI_API_KEY=your-gemini-api-key-here

# CORS (Frontend URL)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173,http://localhost:8080

# Upload Settings
MAX_CONTENT_LENGTH=52428800
UPLOAD_FOLDER=uploads
```

**Get Gemini API Key:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the key and paste in `GEMINI_API_KEY`

**Start the backend server:**
```bash
python app.py
```
✅ Backend now running at **http://localhost:5001**

### 3️⃣ Frontend Setup (5 minutes)

Open a **new terminal** (keep backend running) and:

```bash
# Navigate to frontend folder
cd frontend

# Install Node dependencies
npm install

# Create environment file
touch .env
```

**Configure `.env` file:**
Open `frontend/.env` and add:
```env
# API Configuration
VITE_API_BASE_URL=http://localhost:5001/api

# Google Gemini AI (REQUIRED - same key as backend)
VITE_GEMINI_API_KEY=your-gemini-api-key-here

# Optional: Firebase (for production authentication)
# VITE_FIREBASE_API_KEY=your-firebase-key
# VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
# VITE_FIREBASE_PROJECT_ID=your-project-id
```

**Start the frontend server:**
```bash
npm run dev
```
✅ Frontend now running at **http://localhost:5173**

### 4️⃣ Open Your Browser
Navigate to **http://localhost:5173** and start using the app! 🎉

You should see:
- Beautiful gradient dashboard
- Upload interface (drag & drop files)
- AI processing workflow
- Saved content library

---

## � Project Structure

```
skillsetai/
├── backend/                 # Flask API Server (Python)
│   ├── app.py              # Main application entry point
│   ├── config.py           # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   ├── routes/             # API endpoints
│   │   ├── upload.py       # File/URL upload handling
│   │   ├── processing.py   # Content processing
│   │   ├── accessibility.py # Accessibility features
│   │   ├── survey.py       # User surveys
│   │   └── user.py         # User management
│   ├── services/           # Business logic
│   │   ├── document_processor.py   # Document parsing
│   │   ├── url_processor.py        # Web content extraction
│   │   ├── tts_service.py          # Text-to-speech
│   │   ├── accessibility_service.py # Accessibility features
│   │   └── firebase_service.py      # Firebase integration
│   ├── uploads/            # Uploaded files (gitignored)
│   ├── temp/               # Temporary files (gitignored)
│   ├── venv/               # Python virtual environment (gitignored)
│   └── .env                # Environment variables (gitignored)
│
├── frontend/               # Vue 3 Application
│   ├── src/
│   │   ├── views/         # Page components
│   │   │   ├── DashboardHome.vue   # Main dashboard
│   │   │   ├── UploadPage.vue      # File/URL upload
│   │   │   ├── ProcessPage.vue     # 3-step AI workflow ⭐
│   │   │   ├── SavedContent.vue    # Saved items library ⭐
│   │   │   ├── ProfilePage.vue     # User profile
│   │   │   ├── SettingsPage.vue    # App settings
│   │   │   └── HistoryPage.vue     # Upload history
│   │   ├── layouts/       # Layout components
│   │   │   └── DashboardLayout.vue # Main app shell
│   │   ├── services/      # API integration
│   │   │   ├── gemini.service.js   # Gemini AI client ⭐
│   │   │   ├── api.service.js      # Backend API client
│   │   │   └── firebase.js         # Firebase config
│   │   ├── stores/        # State management (Pinia)
│   │   │   ├── auth.js    # Authentication state
│   │   │   ├── content.js # Content & uploads ⭐
│   │   │   └── theme.js   # Theme & accessibility
│   │   ├── router/        # Vue Router config
│   │   │   └── index.js   # Routes & navigation
│   │   ├── App.vue        # Root component
│   │   ├── main.js        # Application entry point
│   │   └── style.css      # Global styles
│   ├── public/            # Static assets
│   ├── .env               # Environment variables (gitignored)
│   ├── package.json       # Node dependencies
│   ├── tailwind.config.js # Tailwind CSS config
│   ├── postcss.config.js  # PostCSS config
│   └── vite.config.js     # Vite bundler config
│
├── .gitignore             # Git ignore rules
└── README.md              # This file

⭐ = Key files with full AI implementation
```

---

## 🎨 Design Features

### **Color Scheme**
- **Primary Gradient**: Blue (`#0ea5e9` → `#0284c7`)
- **Accent Gradient**: Purple (`#d946ef` → `#c026d3`)
- **Background**: 
  - Light: Gray-50 (`#f9fafb`)
  - Dark: Gray-900 (`#111827`)

### **Typography**
- **Main Font**: Poppins (weights: 300, 400, 500, 600, 700)
- **Dyslexia Font**: OpenDyslexic (loaded via CDN)
- **Responsive**: Scales beautifully on all devices

### **Components**
- Gradient buttons with hover effects
- Card shadows and borders
- Smooth transitions and animations
- Loading states
- Error handling
- Empty states
- Toast notifications (ready to implement)

---

## 🎨 Features

### 1. **Upload Content**
- **Drag & Drop** files (PDF, DOCX, TXT, images)
- **Paste URLs** to extract web content
- Supports up to **50MB** files
- Beautiful animated upload interface
- File type validation

### 2. **User Survey** (Step 1)
- Select **reading level** (5th, 8th, or 10th grade)
- Choose **accessibility features**:
  - ✅ Text-to-Speech
  - ✅ Dyslexia-friendly font
  - ✅ High contrast mode
  - ✅ Image descriptions
- Specify **content type** (article, textbook, research paper, etc.)
- Define **learning goals**

### 3. **AI Processing** (Step 2) - Powered by Gemini AI ⚡
Real-time processing with visual progress indicators:
1. **Reading Document** - Extract text content
2. **Simplifying Text** - Rewrite using Gemini AI
3. **Generating Summary** - Create concise overview
4. **Extracting Key Points** - Identify main concepts
5. **Finalizing** - Prepare results

**Uses real Gemini AI API calls:**
```javascript
const simplified = await geminiService.simplifyText(text, level);
const summary = await geminiService.generateSummary(text);
const keyPoints = await geminiService.extractKeyPoints(text);
```

### 4. **View Results** (Step 3)
- **Simplified Content** - Easy-to-read version
- **Summary** - Quick overview
- **Key Points** - Numbered list of main ideas
- **Copy to Clipboard** - One-click copy
- **Save for Later** - Store in your library

### 5. **Saved Content Library**
- View all saved items in beautiful grid layout
- Click to open modal with full content
- Search and filter (coming soon)
- Delete unwanted content
- Copy all content (simplified + summary + key points)
- Relative timestamps ("2 minutes ago", "1 hour ago")

### 6. **Theme & Accessibility**
- 🌙 **Dark/Light Mode** - Toggle with smooth transitions
- 📖 **Dyslexia Font** - OpenDyslexic font option
- 🔍 **Font Size Control** - Small to Extra Large
- 🎨 **High Contrast** - Enhanced visibility
- ⌨️ **Keyboard Navigation** - Full accessibility

### 7. **Responsive Design**
- Mobile-first approach
- Works on phones, tablets, and desktops
- Collapsible sidebar navigation
- Touch-friendly interfaces

---

## 🧪 Testing the Application

### 1. **Verify Servers are Running**

**Backend:**
```bash
# Should see:
# * Running on http://127.0.0.1:5001
curl http://localhost:5001/api/health
# Expected: {"status":"healthy"}
```

**Frontend:**
```bash
# Should see:
# Local: http://localhost:5173/
# Open your browser to this URL
```

### 2. **Test File Upload**
1. Open http://localhost:5173
2. You'll land directly on dashboard (no login required in demo mode)
3. Click **"Upload"** in sidebar
4. Drag & drop a text file, PDF, or DOCX
5. File should upload successfully

### 3. **Test AI Processing Workflow**
1. After upload, you'll be redirected to **Process page**
2. **Step 1 - Survey:**
   - Select reading level (e.g., "5th Grade")
   - Enable features (Text-to-Speech, Dyslexia Font)
   - Choose content type (e.g., "Article")
   - Enter learning goal
   - Click **"Continue to AI Processing"**

3. **Step 2 - AI Processing:**
   - Watch the 5 stages progress:
     - ✅ Reading document
     - ✅ Simplifying text (real Gemini AI call)
     - ✅ Generating summary (real Gemini AI call)
     - ✅ Extracting key points (real Gemini AI call)
     - ✅ Finalizing
   - Should take 5-15 seconds depending on content length

4. **Step 3 - Results:**
   - View **Simplified Content** - text rewritten by AI
   - Read **Summary** - AI-generated overview
   - See **Key Points** - numbered list from AI
   - Click **"Copy All"** to copy to clipboard
   - Click **"Save Content"** to add to library

### 4. **Test Saved Content**
1. Click **"Saved Content"** in sidebar
2. See grid of saved items
3. Click any item to open modal with full content
4. Test **Delete** button (confirms before deleting)
5. Test **Copy All** button in modal

### 5. **Test Dark Mode**
- Click the moon/sun icon in header
- Theme should smoothly transition
- All colors should adapt properly
- Test navigation in dark mode

### 6. **Test Responsive Design**
- Resize browser window
- Sidebar should collapse on mobile
- Grid should adjust columns
- Touch-friendly on mobile devices

---

## � Troubleshooting

### Backend Issues

**Backend won't start:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt

# Check if port 5001 is free
lsof -ti:5001  # macOS/Linux - if shows PID, kill it
netstat -ano | findstr :5001  # Windows
```

**Import errors:**
```bash
# Make sure you're in backend directory
cd backend
# Activate venv
source venv/bin/activate
# Install missing packages
pip install flask flask-cors python-dotenv
```

**"No module named 'routes'" error:**
```bash
# Make sure backend/__init__.py files exist
touch routes/__init__.py
touch services/__init__.py
```

### Frontend Issues

**Frontend won't start:**
```bash
# Delete node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install

# Check if port 5173 is free
lsof -ti:5173  # macOS/Linux
```

**Tailwind classes not working:**
```bash
# Restart dev server
npm run dev

# Clear browser cache (Cmd+Shift+R / Ctrl+Shift+R)

# Check tailwind.config.js content paths:
content: [
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
]
```

**"Module not found" errors:**
```bash
# Reinstall dependencies
npm install

# Clear Vite cache
rm -rf node_modules/.vite
npm run dev
```

### CORS Errors

**"Access-Control-Allow-Origin" errors:**
1. Make sure backend is running on **port 5001**
2. Frontend should be on **port 5173**
3. Check `backend/config.py`:
```python
CORS_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:5173',  # Add this
    'http://localhost:8080'
]
```
4. Restart backend server

### Gemini API Errors

**"API key not valid" error:**
- Verify API key is correct in both `.env` files (backend and frontend)
- Get new key at https://makersuite.google.com/app/apikey
- Make sure there are no quotes or extra spaces
- Format: `GEMINI_API_KEY=AIzaSy...`

**"Quota exceeded" error:**
- Check quota at https://makersuite.google.com
- Free tier: 60 requests per minute
- Wait a minute and try again

**"Model not found" error:**
- Check you're using correct model name: `gemini-2.0-flash-exp`
- Update `frontend/src/services/gemini.service.js` if needed

### Upload Issues

**"File too large" error:**
- Default limit is 50MB
- Check `backend/config.py`: `MAX_CONTENT_LENGTH`
- Increase if needed (in bytes): `100 * 1024 * 1024` = 100MB

**Upload hangs or fails:**
- Check backend console for errors
- Verify `uploads/` folder exists in backend
- Check file permissions: `chmod -R 755 uploads/`

### Dark Mode Not Working

1. Open browser DevTools (F12)
2. Check Console for errors
3. Verify `useThemeStore` is imported
4. Clear localStorage: `localStorage.clear()` in Console
5. Refresh page

## 📚 Tech Stack

### Frontend
- **Vue 3** - Progressive JavaScript framework (Composition API)
- **Vite 7** - Next-generation build tool (fast HMR)
- **Tailwind CSS 3** - Utility-first CSS framework
- **Pinia** - Vue state management library
- **Vue Router 4** - Official router for Vue.js
- **Axios** - Promise-based HTTP client
- **@google/generative-ai** - Google Gemini AI SDK

### Backend
- **Flask 3.0** - Lightweight Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **python-docx** - Microsoft Word document processing
- **PyPDF2** - PDF file parsing
- **beautifulsoup4** - HTML/XML parsing
- **validators** - URL and data validation
- **python-dotenv** - Environment variable management

### AI & Services
- **Google Gemini AI** - Advanced language model (gemini-2.0-flash-exp)
- **Firebase** (optional) - Authentication, Firestore database, Cloud Storage

## 📋 API Endpoints

### Upload
- `POST /api/upload/document` - Upload file (PDF, DOCX, TXT, images)
- `POST /api/upload/url` - Process web URL

### Accessibility
- `POST /api/accessibility/simplify-text` - Simplify text
- `POST /api/accessibility/text-to-speech` - Generate audio
- `POST /api/accessibility/image-alt-text` - Get image descriptions

### Health
- `GET /api/health` - Check API status

## 🎯 Use Cases

### For Students 🎓
- Simplify complex textbooks to grade-appropriate level
- Get quick summaries of research papers
- Listen to study materials with text-to-speech
- Extract key concepts for exam prep

### For Educators 👨‍🏫
- Make course content accessible for all students
- Generate different reading level versions
- Create auto-generated study guides
- Support diverse learning needs

### For Content Creators ✍️
- Make blog articles more accessible
- Generate alt-text for images automatically
- Create audio versions of text content
- Reach wider audiences

## 🚀 Deployment

### Frontend (Vercel / Netlify)

**Build command:**
```bash
cd frontend
npm run build
```

Deploy the `frontend/dist/` folder and set environment variables (`VITE_*` from `.env`).

### Backend (Heroku / Railway / Render)

1. Set all environment variables from `.env`
2. Set `FLASK_ENV=production`
3. Use Gunicorn: `pip install gunicorn`
4. Create `Procfile`: `web: gunicorn app:app`

See `backend/DEPLOYMENT.md` for detailed instructions.

## 🛣️ Roadmap

### ✅ Completed
- [x] File upload (PDF, DOCX, TXT, images)
- [x] URL content extraction
- [x] AI text simplification (Gemini)
- [x] Summary generation (Gemini)
- [x] Key points extraction (Gemini)
- [x] 3-step processing workflow
- [x] Save & review content library
- [x] Dark mode
- [x] Responsive design
- [x] Demo mode (no authentication)

### 🚧 Planned
- [ ] Real text-to-speech implementation
- [ ] Firebase authentication
- [ ] PDF viewer with highlighting
- [ ] Math equation processing
- [ ] Multi-language support
- [ ] Search and filter saved content
- [ ] Export to PDF/DOCX
- [ ] Mobile app

## 🤝 Contributing

Contributions welcome!

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📞 Support & Documentation
1. Landing Page (/) 
   ↓ Click "Get Started"
   
2. Register Page (/register)
   ↓ Create account
   
3. Survey Page (/dashboard/survey) - First time only
   ↓ Complete accessibility preferences
   
4. Dashboard Home (/dashboard)
   ↓ See stats, recent activity
   
5. Upload Page (/dashboard/upload)
   ↓ Drag file or paste URL
   
6. Process Page (/dashboard/process/:id)
   ↓ Choose simplification level, enable TTS
   
7. Content Viewer (/dashboard/content/:id)
   ↓ View accessible content
   
8. Save → Saved Content (/dashboard/saved)
   
9. Profile (/dashboard/profile) - Manage account
   
10. Settings (/dashboard/settings) - Accessibility options
```

---

## 💡 Pro Tips

### **Development**
```bash
# Backend hot reload
cd backend
flask run --reload

# Frontend hot reload (already enabled)
cd frontend
npm run dev
```

### **State Management**
```javascript
// Always use Pinia stores for global state
import { useAuthStore } from '@/stores/auth';
const authStore = useAuthStore();

// User data
authStore.user

// Check if logged in
authStore.isLoggedIn
```

### **API Calls**
```javascript
import { apiService } from '@/services/api.service';

// Always use try-catch
try {
  const result = await apiService.uploadDocument(file, userId);
  console.log('Success:', result.data);
} catch (error) {
  console.error('Error:', error.response?.data);
}
```

### **Styling**
```vue
<!-- Use Tailwind utility classes -->
<div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md">
  <!-- Content -->
</div>

<!-- For complex styles, use @apply in style section -->
<style scoped>
.custom-button {
  @apply px-6 py-3 bg-gradient-to-r from-primary-600 to-accent-600 text-white rounded-lg;
}
</style>
```

---

## 🐛 Troubleshooting

### **Frontend won't start**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### **Tailwind classes not working**
- Check `tailwind.config.js` content paths
- Restart dev server
- Clear browser cache

### **Firebase errors**
- Verify `.env` has all Firebase keys
- Check Firebase console for enabled features
- Ensure Firestore rules allow read/write

### **Backend connection fails**
- Ensure backend is running: `http://localhost:5001/api/health`
- Check CORS settings
- Verify `VITE_API_BASE_URL` in `.env`

---

## 🎨 Screenshots (What You'll See)

### **Landing Page**
- Beautiful gradient hero with "Transform Learning Materials For Everyone"
- Feature cards (AI simplification, TTS, Image descriptions)
- Call-to-action buttons

### **Login/Register**
- Clean forms with gradient branding
- Error handling
- Smooth transitions

### **Dashboard**
- Sidebar navigation (collapsible on mobile)
- Stats cards
- Recent activity
- Quick action buttons

### **Upload Page**
- Drag & drop zone with animations
- File preview
- Progress bar
- Tab switching (File vs URL)

---

## 🚀 Deployment

### **Frontend** (Vercel/Netlify)
```bash
cd frontend
npm run build

# Deploy dist/ folder to Vercel/Netlify
```

### **Backend** (Heroku/Railway)
```bash
cd backend
# See backend/DEPLOYMENT.md
```

---

## 📞 Support & Documentation

- **Backend API Docs**: See `backend/API_DOCUMENTATION.md`
- **Backend Endpoints Summary**: See `backend/ENDPOINTS_SUMMARY.md`
- **Project Overview**: See `backend/PROJECT_OVERVIEW.md`
- **Deployment Guide**: See `backend/DEPLOYMENT.md`

## 🙏 Acknowledgments

- **Google Gemini** - Powerful AI capabilities for text processing
- **Vue.js Team** - Amazing reactive framework
- **Tailwind CSS** - Beautiful utility-first styling
- **Flask** - Lightweight and flexible web framework
- **Open Source Community** - Inspiration and tools

## 📄 License

This project is licensed under the **MIT License** - see LICENSE file for details.

## 💡 Pro Tips

### For Development
- Use **Chrome DevTools** (F12) for debugging
- **Console tab** shows JavaScript errors
- **Network tab** shows API requests/responses
- **Vue DevTools** extension for state inspection
- Backend logs appear in terminal running Flask

### For Better Performance
- Keep file sizes under 10MB for faster processing
- Use simple reading level for longer documents
- Close unused browser tabs
- Use production build for deployment

### For Accessibility Testing
- Test with screen readers (NVDA, JAWS, VoiceOver)
- Try keyboard navigation (Tab, Enter, Escape)
- Check color contrast ratios
- Test on different devices and browsers

---

## 🎉 You're All Set!

Your accessibility learning platform is ready to go!

### Quick Commands Reminder:

**Start Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

**Start Frontend:**
```bash
cd frontend
npm run dev
```

**Access App:**
```
http://localhost:5173
```

---

**Made with ❤️ for accessibility**

*Making education accessible to everyone, one document at a time.* 🌟
