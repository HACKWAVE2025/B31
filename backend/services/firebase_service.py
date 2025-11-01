"""
Firebase Authentication Service
Handles user authentication, signup, signin
"""

import firebase_admin
from firebase_admin import credentials, auth, firestore
from config import Config
import os

class FirebaseService:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseService, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not FirebaseService._initialized:
            self.initialize()
            FirebaseService._initialized = True
    
    def initialize(self):
        """Initialize Firebase Admin SDK"""
        try:
            cred_path = Config.FIREBASE_CREDENTIALS_PATH
            if cred_path and os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                print("Firebase initialized successfully")
            else:
                print("Warning: Firebase credentials not found. Some features may not work.")
                self.db = None
        except Exception as e:
            print(f"Firebase initialization error: {e}")
            self.db = None
    
    def verify_token(self, id_token):
        """Verify Firebase ID token"""
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception as e:
            raise ValueError(f"Invalid token: {str(e)}")
    
    def get_user(self, uid):
        """Get user by UID"""
        try:
            user = auth.get_user(uid)
            return {
                'uid': user.uid,
                'email': user.email,
                'display_name': user.display_name,
                'photo_url': user.photo_url,
                'email_verified': user.email_verified
            }
        except Exception as e:
            raise ValueError(f"User not found: {str(e)}")
    
    def create_user(self, email, password, display_name=None):
        """Create a new user"""
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=display_name
            )
            
            # Create user profile in Firestore
            if self.db:
                self.db.collection('users').document(user.uid).set({
                    'email': email,
                    'display_name': display_name,
                    'created_at': firestore.SERVER_TIMESTAMP,
                    'preferences': {
                        'theme': 'light',
                        'dyslexia_font': False,
                        'high_contrast': False,
                        'text_size': 'medium',
                        'tts_voice': 'default',
                        'tts_speed': 1.0
                    },
                    'accessibility_needs': []
                })
            
            return user.uid
        except Exception as e:
            raise ValueError(f"Error creating user: {str(e)}")
    
    def update_user_profile(self, uid, data):
        """Update user profile in Firestore"""
        try:
            if self.db:
                self.db.collection('users').document(uid).update(data)
                return True
            return False
        except Exception as e:
            raise ValueError(f"Error updating profile: {str(e)}")
    
    def get_user_profile(self, uid):
        """Get user profile from Firestore"""
        try:
            if self.db:
                doc = self.db.collection('users').document(uid).get()
                if doc.exists:
                    return doc.to_dict()
            return None
        except Exception as e:
            raise ValueError(f"Error getting profile: {str(e)}")
    
    def save_user_history(self, uid, history_item):
        """Save processing history for user"""
        try:
            if self.db:
                self.db.collection('users').document(uid).collection('history').add({
                    **history_item,
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
                return True
            return False
        except Exception as e:
            raise ValueError(f"Error saving history: {str(e)}")
    
    def get_user_history(self, uid, limit=50):
        """Get user processing history"""
        try:
            if self.db:
                docs = self.db.collection('users').document(uid).collection('history')\
                    .order_by('timestamp', direction=firestore.Query.DESCENDING)\
                    .limit(limit).stream()
                return [doc.to_dict() for doc in docs]
            return []
        except Exception as e:
            raise ValueError(f"Error getting history: {str(e)}")
    
    def save_content(self, uid, content_data):
        """Save generated content for user"""
        try:
            if self.db:
                doc_ref = self.db.collection('users').document(uid).collection('saved_content').add({
                    **content_data,
                    'saved_at': firestore.SERVER_TIMESTAMP
                })
                return doc_ref[1].id
            return None
        except Exception as e:
            raise ValueError(f"Error saving content: {str(e)}")
    
    def get_saved_content(self, uid, limit=50):
        """Get user's saved content"""
        try:
            if self.db:
                docs = self.db.collection('users').document(uid).collection('saved_content')\
                    .order_by('saved_at', direction=firestore.Query.DESCENDING)\
                    .limit(limit).stream()
                return [{'id': doc.id, **doc.to_dict()} for doc in docs]
            return []
        except Exception as e:
            raise ValueError(f"Error getting saved content: {str(e)}")


# Singleton instance
firebase_service = FirebaseService()
