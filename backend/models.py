"""
Database Models for Accessibility Learning Hub
PostgreSQL models using SQLAlchemy
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON

db = SQLAlchemy()


class User(db.Model):
    """User model - synced with Firebase Auth"""
    __tablename__ = 'users'
    
    id = db.Column(db.String(128), primary_key=True)  # Firebase UID
    email = db.Column(db.String(255), unique=True, nullable=False)
    display_name = db.Column(db.String(255))
    
    # Survey data
    survey_data = db.Column(JSON)  # Store survey responses
    survey_completed = db.Column(db.Boolean, default=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    uploads = db.relationship('Upload', backref='user', lazy=True, cascade='all, delete-orphan')
    saved_content = db.relationship('SavedContent', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'displayName': self.display_name,
            'surveyData': self.survey_data,
            'surveyCompleted': self.survey_completed,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }


class Upload(db.Model):
    """Uploaded files and URLs"""
    __tablename__ = 'uploads'
    
    id = db.Column(db.String(128), primary_key=True)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False)
    
    # File/URL info
    filename = db.Column(db.String(255))
    file_type = db.Column(db.String(50))
    file_size = db.Column(db.Integer)
    url = db.Column(db.Text)
    
    # Content
    text_content = db.Column(db.Text)
    title = db.Column(db.String(500))
    
    # Metadata
    upload_type = db.Column(db.String(20))  # 'file' or 'url'
    status = db.Column(db.String(20), default='pending')  # pending, processing, completed, error
    
    # Timestamps
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    processed_at = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'filename': self.filename,
            'fileType': self.file_type,
            'fileSize': self.file_size,
            'url': self.url,
            'textContent': self.text_content,
            'title': self.title,
            'uploadType': self.upload_type,
            'status': self.status,
            'uploadedAt': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'processedAt': self.processed_at.isoformat() if self.processed_at else None
        }


class SavedContent(db.Model):
    """Processed and saved content"""
    __tablename__ = 'saved_content'
    
    id = db.Column(db.String(128), primary_key=True)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), nullable=False)
    upload_id = db.Column(db.String(128), db.ForeignKey('uploads.id'))
    
    # Original content
    file_name = db.Column(db.String(255))
    original_text = db.Column(db.Text)
    
    # Processed content
    simplified_text = db.Column(db.Text)
    summary = db.Column(db.Text)
    key_points = db.Column(JSON)  # Store as JSON array
    
    # Processing metadata
    reading_level = db.Column(db.String(50))
    content_type = db.Column(db.String(50))
    accessibility_features = db.Column(JSON)  # Store enabled features
    
    # Timestamps
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'uploadId': self.upload_id,
            'fileName': self.file_name,
            'originalText': self.original_text,
            'simplifiedText': self.simplified_text,
            'summary': self.summary,
            'keyPoints': self.key_points,
            'readingLevel': self.reading_level,
            'contentType': self.content_type,
            'accessibilityFeatures': self.accessibility_features,
            'savedAt': self.saved_at.isoformat() if self.saved_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }


class UserPreferences(db.Model):
    """User accessibility preferences and settings"""
    __tablename__ = 'user_preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), db.ForeignKey('users.id'), unique=True, nullable=False)
    
    # Accessibility preferences
    default_reading_level = db.Column(db.String(50), default='simple')
    text_to_speech_enabled = db.Column(db.Boolean, default=True)
    dyslexia_font_enabled = db.Column(db.Boolean, default=False)
    high_contrast_enabled = db.Column(db.Boolean, default=False)
    image_descriptions_enabled = db.Column(db.Boolean, default=True)
    
    # UI preferences
    theme = db.Column(db.String(20), default='light')  # light, dark
    font_size = db.Column(db.String(20), default='medium')  # small, medium, large, xl
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'userId': self.user_id,
            'defaultReadingLevel': self.default_reading_level,
            'textToSpeechEnabled': self.text_to_speech_enabled,
            'dyslexiaFontEnabled': self.dyslexia_font_enabled,
            'highContrastEnabled': self.high_contrast_enabled,
            'imageDescriptionsEnabled': self.image_descriptions_enabled,
            'theme': self.theme,
            'fontSize': self.font_size,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None
        }
