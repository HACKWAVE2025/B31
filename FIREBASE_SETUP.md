# 🔥 Firebase Authentication Setup Guide

## 🚨 IMPORTANT: Follow these steps to enable Google Sign-In

### Step 1: Enable Google Sign-In Provider in Firebase Console

1. **Go to Firebase Console**: https://console.firebase.google.com/
2. **Select your project**: `skillset-ai`
3. **Navigate to Authentication**:
   - Click on "Authentication" in the left sidebar
   - Click on "Sign-in method" tab
4. **Enable Google Provider**:
   - Click on "Google" in the Sign-in providers list
   - Toggle "Enable" to ON
   - **Set Support Email**: Add your email address (required)
   - Click "Save"

### Step 2: Enable Email/Password Sign-In (if not already enabled)

1. In the same "Sign-in method" tab
2. Click on "Email/Password"
3. Toggle "Enable" to ON
4. Click "Save"

### Step 3: Add Authorized Domains

1. Still in "Sign-in method" tab
2. Scroll down to "Authorized domains"
3. Make sure these domains are listed:
   - `localhost` ✅ (should be there by default)
   - Your production domain (e.g., `skillsetai.vercel.app`) when you deploy

### Step 4: Verify Configuration

Your Firebase config in `.env` file:
```env
VITE_FIREBASE_API_KEY=AIzaSyCuwa_pL7gpT88PKMhE1JbxzoqLKStIakE
VITE_FIREBASE_AUTH_DOMAIN=skillset-ai.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=skillset-ai
VITE_FIREBASE_STORAGE_BUCKET=skillset-ai.firebasestorage.app
VITE_FIREBASE_MESSAGING_SENDER_ID=579581501759
VITE_FIREBASE_APP_ID=1:579581501759:web:298307dfeafa9b97f4338a
VITE_FIREBASE_MEASUREMENT_ID=G-TZB4SJZC5C
```

## ✅ Testing Authentication

### Test Email/Password Sign-Up:
1. Go to http://localhost:5173
2. Click "Get Started"
3. Click "Sign Up"
4. Fill in:
   - Name: Test User
   - Email: test@example.com
   - Password: Test@123 (must have 8+ chars, 1 number, 1 special char)
5. Click "Create Account"

### Test Email/Password Sign-In:
1. Click "Sign In" (if you created an account above)
2. Enter your email and password
3. Click "Sign In"

### Test Google Sign-In:
1. Click "Sign in with Google" button
2. Select your Google account
3. You should be redirected to the dashboard

## 🐛 Common Errors & Solutions

### Error: "auth/operation-not-allowed"
**Solution**: Google sign-in is not enabled in Firebase Console. Follow Step 1 above.

### Error: "auth/popup-blocked"
**Solution**: Your browser is blocking popups. Allow popups for localhost.

### Error: "auth/unauthorized-domain"
**Solution**: Add your domain to Authorized domains in Firebase Console (Step 3).

### Error: "auth/weak-password"
**Solution**: Password must be at least 8 characters with:
- At least 1 number
- At least 1 special character (!@#$%^&*)

### Error: "auth/email-already-in-use"
**Solution**: This email is already registered. Try signing in instead.

### Error: Backend connection failed
**Solution**: Make sure backend is running on port 5001:
```bash
cd backend
source venv/bin/activate
python app.py
```

## 🔍 Debug Console Messages

When you sign in/up, you should see these console messages:

**Sign-Up:**
```
🔵 Creating user account...
✅ User created: [uid]
✅ Profile updated with name: [name]
✅ User synced to database
```

**Sign-In:**
```
🔵 Signing in user...
✅ Sign-in successful: [email]
```

**Google Sign-In:**
```
🔵 Initiating Google sign-in...
✅ Google sign-in successful: [email]
✅ User synced to database
```

## 📝 What I Fixed

1. ✅ **AuthModal v-model binding**: Fixed modal not showing/hiding properly
2. ✅ **Better error handling**: Added detailed error messages for all auth operations
3. ✅ **Console logging**: Added debug logs to track authentication flow
4. ✅ **Google provider config**: Added `prompt: 'select_account'` for better UX
5. ✅ **Database sync error handling**: Auth works even if backend is offline
6. ✅ **Additional error codes**: Handle popup-blocked, unauthorized-domain, too-many-requests, etc.

## 🚀 Next Steps

1. **Enable Google Sign-In** in Firebase Console (CRITICAL!)
2. Test all authentication methods
3. If you deploy to production, add your domain to Firebase authorized domains
4. Consider enabling other providers (GitHub, Microsoft, etc.)

## 📞 Need Help?

If authentication still doesn't work after following these steps:

1. Open browser console (F12) and check for errors
2. Look for the error code (e.g., `auth/operation-not-allowed`)
3. Check the error messages in the "Common Errors" section above
4. Verify Firebase Console settings match this guide
