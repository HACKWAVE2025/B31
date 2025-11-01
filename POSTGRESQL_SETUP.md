# PostgreSQL Database Setup Guide

## 🗄️ Database Integration Overview

Your Accessibility Learning Hub now uses **PostgreSQL** for persistent data storage, integrated with Firebase Authentication.

### What's Been Added:

✅ **PostgreSQL Database Models:**
- `users` - User accounts (synced with Firebase Auth)
- `uploads` - File and URL uploads
- `saved_content` - Processed and saved content
- `user_preferences` - Accessibility settings

✅ **Backend API Routes:**
- `/api/db/users` - User management
- `/api/db/uploads` - Upload CRUD
- `/api/db/saved-content` - Saved content CRUD
- `/api/db/preferences` - User preferences
- `/api/db/stats` - User statistics

✅ **Frontend Integration:**
- `database.service.js` - Database API client
- Updated `content.js` store to use PostgreSQL

---

## 📋 Prerequisites

Before setting up the database, ensure you have:

1. **PostgreSQL installed** (version 12 or higher)
2. **Python 3.12+** with pip
3. **Node.js 18+** for frontend

---

## 🚀 Quick Setup

### Step 1: Install PostgreSQL

#### macOS (using Homebrew):
```bash
brew install postgresql@15
brew services start postgresql@15
```

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### Windows:
Download from: https://www.postgresql.org/download/windows/

### Step 2: Create Database

Run the automated setup script:

```bash
cd backend
./setup_database.sh
```

**Or manually:**

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE skillsetai_db;

# Exit
\q
```

### Step 3: Install Python Dependencies

```bash
cd backend
pip install psycopg2-binary Flask-SQLAlchemy Flask-Migrate
```

### Step 4: Configure Environment

Update `backend/.env`:

```env
# PostgreSQL Database
DATABASE_URL=postgresql://postgres@localhost:5432/skillsetai_db

# Or with password:
# DATABASE_URL=postgresql://username:password@localhost:5432/skillsetai_db
```

### Step 5: Initialize Database Tables

```bash
cd backend
python3 << 'EOF'
from app import create_app
from models import db

app = create_app()
with app.app_context():
    db.create_all()
    print("✅ Database tables created!")
EOF
```

### Step 6: Start Backend

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

✅ Backend running with PostgreSQL at **http://localhost:5001**

---

## 🔧 Database Schema

### `users` Table
```sql
- id (VARCHAR) - Firebase UID (Primary Key)
- email (VARCHAR) - User email
- display_name (VARCHAR) - Display name
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### `uploads` Table
```sql
- id (VARCHAR) - Upload ID (Primary Key)
- user_id (VARCHAR) - Foreign Key to users
- filename (VARCHAR)
- file_type (VARCHAR)
- file_size (INTEGER)
- url (TEXT)
- text_content (TEXT)
- title (VARCHAR)
- upload_type (VARCHAR) - 'file' or 'url'
- status (VARCHAR)
- uploaded_at (TIMESTAMP)
- processed_at (TIMESTAMP)
```

### `saved_content` Table
```sql
- id (VARCHAR) - Content ID (Primary Key)
- user_id (VARCHAR) - Foreign Key to users
- upload_id (VARCHAR) - Foreign Key to uploads
- file_name (VARCHAR)
- original_text (TEXT)
- simplified_text (TEXT)
- summary (TEXT)
- key_points (JSON) - Array of key points
- reading_level (VARCHAR)
- content_type (VARCHAR)
- accessibility_features (JSON)
- saved_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### `user_preferences` Table
```sql
- id (INTEGER) - Auto-increment
- user_id (VARCHAR) - Foreign Key to users (Unique)
- default_reading_level (VARCHAR)
- text_to_speech_enabled (BOOLEAN)
- dyslexia_font_enabled (BOOLEAN)
- high_contrast_enabled (BOOLEAN)
- image_descriptions_enabled (BOOLEAN)
- theme (VARCHAR) - 'light' or 'dark'
- font_size (VARCHAR)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

---

## 📡 API Endpoints

### User Operations
- `POST /api/db/users` - Create/update user
- `GET /api/db/users/{userId}` - Get user

### Upload Operations
- `POST /api/db/uploads` - Save upload
- `GET /api/db/uploads/{userId}` - Get user uploads
- `DELETE /api/db/uploads/{uploadId}` - Delete upload

### Saved Content Operations
- `POST /api/db/saved-content` - Save content
- `GET /api/db/saved-content/{userId}` - Get saved content
- `GET /api/db/saved-content/item/{contentId}` - Get specific item
- `DELETE /api/db/saved-content/{contentId}` - Delete content

### Preferences Operations
- `GET /api/db/preferences/{userId}` - Get preferences
- `PUT /api/db/preferences/{userId}` - Update preferences

### Stats Operations
- `GET /api/db/stats/{userId}` - Get user statistics

---

## 🔄 How It Works

### 1. **User Signs In with Firebase**
```javascript
// Firebase handles authentication
const user = await signInWithEmailAndPassword(auth, email, password);

// Create user in PostgreSQL database
await databaseService.createUser({
  id: user.uid,
  email: user.email,
  displayName: user.displayName
});
```

### 2. **Upload File**
```javascript
// Upload file to backend
const upload = await apiService.uploadDocument(file, userId);

// Save to PostgreSQL
await databaseService.saveUpload({
  userId: userId,
  filename: file.name,
  fileType: file.type,
  textContent: upload.textContent
});
```

### 3. **Process and Save Content**
```javascript
// Process with Gemini AI
const simplified = await geminiService.simplifyText(text, level);

// Save to PostgreSQL
await databaseService.saveContent({
  userId: userId,
  fileName: fileName,
  simplifiedText: simplified,
  summary: summary,
  keyPoints: keyPoints
});
```

### 4. **Fetch User Data**
```javascript
// Load all user data on login
await contentStore.fetchUserContent(userId);

// Loads uploads and saved content from PostgreSQL
```

---

## 🧪 Testing the Database

### 1. Connect to PostgreSQL
```bash
psql -U postgres -d skillsetai_db
```

### 2. List Tables
```sql
\dt
```

### 3. View Users
```sql
SELECT * FROM users;
```

### 4. View Uploads
```sql
SELECT id, filename, upload_type, uploaded_at FROM uploads;
```

### 5. View Saved Content
```sql
SELECT id, file_name, reading_level, saved_at FROM saved_content;
```

---

## 🐛 Troubleshooting

### "Connection refused" error
```bash
# Check if PostgreSQL is running
brew services list  # macOS
sudo systemctl status postgresql  # Linux

# Restart PostgreSQL
brew services restart postgresql@15  # macOS
sudo systemctl restart postgresql  # Linux
```

### "FATAL: database does not exist"
```bash
# Create database manually
psql -U postgres -c "CREATE DATABASE skillsetai_db;"
```

### "FATAL: role does not exist"
```bash
# Create PostgreSQL user
psql -U postgres -c "CREATE USER yourusername WITH PASSWORD 'yourpassword';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE skillsetai_db TO yourusername;"
```

### Python import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 🔐 Production Configuration

For production, use environment variables:

```env
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### Heroku/Railway
Database URL is automatically provided - no configuration needed!

### Custom Server
```bash
# Set strong password
export DATABASE_URL="postgresql://skillset_user:STRONG_PASSWORD@localhost:5432/skillsetai_db"
```

---

## 📊 Database Migrations (Advanced)

To manage schema changes:

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Add new column"

# Apply migration
flask db upgrade
```

---

## ✅ Verification Checklist

- [ ] PostgreSQL installed and running
- [ ] Database `skillsetai_db` created
- [ ] Python dependencies installed
- [ ] `DATABASE_URL` set in `.env`
- [ ] Database tables created (`db.create_all()`)
- [ ] Backend starts without errors
- [ ] Can connect to database with `psql`

---

## 🎉 Success!

Your app now has a real database! Data persists across sessions and page refreshes.

**Next Steps:**
1. Start backend: `python app.py`
2. Start frontend: `npm run dev`
3. Sign in with Firebase
4. Upload and save content - it's all stored in PostgreSQL! 🚀
