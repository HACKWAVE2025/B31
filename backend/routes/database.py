"""
Database Routes - CRUD operations for saved content and uploads
"""
from flask import Blueprint, request, jsonify
from models import db, User, Upload, SavedContent, UserPreferences
from datetime import datetime
import uuid

db_bp = Blueprint('database', __name__)


# ==================== USER ROUTES ====================

@db_bp.route('/users', methods=['POST'])
def create_user():
    """Create or update user from Firebase Auth"""
    data = request.json
    
    try:
        user = User.query.get(data['id'])
        
        if user:
            # Update existing user
            user.email = data.get('email', user.email)
            user.display_name = data.get('displayName', user.display_name)
            user.updated_at = datetime.utcnow()
        else:
            # Create new user
            user = User(
                id=data['id'],
                email=data['email'],
                display_name=data.get('displayName')
            )
            db.session.add(user)
            
            # Create default preferences
            preferences = UserPreferences(user_id=user.id)
            db.session.add(preferences)
        
        db.session.commit()
        return jsonify(user.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@db_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


# ==================== UPLOAD ROUTES ====================

@db_bp.route('/uploads', methods=['POST'])
def create_upload():
    """Save upload metadata to database"""
    data = request.json
    
    try:
        upload = Upload(
            id=data.get('id', str(uuid.uuid4())),
            user_id=data['userId'],
            filename=data.get('filename'),
            file_type=data.get('fileType'),
            file_size=data.get('fileSize'),
            url=data.get('url'),
            text_content=data.get('textContent'),
            title=data.get('title'),
            upload_type=data.get('uploadType', 'file'),
            status='completed'
        )
        
        db.session.add(upload)
        db.session.commit()
        
        return jsonify(upload.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@db_bp.route('/uploads/<user_id>', methods=['GET'])
def get_user_uploads(user_id):
    """Get all uploads for a user"""
    try:
        uploads = Upload.query.filter_by(user_id=user_id).order_by(Upload.uploaded_at.desc()).all()
        return jsonify([upload.to_dict() for upload in uploads]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@db_bp.route('/uploads/<upload_id>', methods=['DELETE'])
def delete_upload(upload_id):
    """Delete an upload"""
    try:
        upload = Upload.query.get(upload_id)
        if not upload:
            return jsonify({'error': 'Upload not found'}), 404
        
        db.session.delete(upload)
        db.session.commit()
        
        return jsonify({'message': 'Upload deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ==================== SAVED CONTENT ROUTES ====================

@db_bp.route('/saved-content', methods=['POST'])
def save_content():
    """Save processed content"""
    data = request.json
    
    try:
        content = SavedContent(
            id=data.get('id', str(uuid.uuid4())),
            user_id=data['userId'],
            upload_id=data.get('uploadId'),
            file_name=data.get('fileName'),
            original_text=data.get('originalText'),
            simplified_text=data.get('simplifiedText'),
            summary=data.get('summary'),
            key_points=data.get('keyPoints', []),
            reading_level=data.get('readingLevel'),
            content_type=data.get('contentType'),
            accessibility_features=data.get('accessibilityFeatures', {})
        )
        
        db.session.add(content)
        db.session.commit()
        
        return jsonify(content.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@db_bp.route('/saved-content/<user_id>', methods=['GET'])
def get_saved_content(user_id):
    """Get all saved content for a user"""
    try:
        content = SavedContent.query.filter_by(user_id=user_id).order_by(SavedContent.saved_at.desc()).all()
        return jsonify([item.to_dict() for item in content]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@db_bp.route('/saved-content/item/<content_id>', methods=['GET'])
def get_saved_content_item(content_id):
    """Get a specific saved content item"""
    try:
        content = SavedContent.query.get(content_id)
        if not content:
            return jsonify({'error': 'Content not found'}), 404
        
        return jsonify(content.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@db_bp.route('/saved-content/<content_id>', methods=['DELETE'])
def delete_saved_content(content_id):
    """Delete saved content"""
    try:
        content = SavedContent.query.get(content_id)
        if not content:
            return jsonify({'error': 'Content not found'}), 404
        
        db.session.delete(content)
        db.session.commit()
        
        return jsonify({'message': 'Content deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ==================== USER PREFERENCES ROUTES ====================

@db_bp.route('/preferences/<user_id>', methods=['GET'])
def get_preferences(user_id):
    """Get user preferences"""
    try:
        prefs = UserPreferences.query.filter_by(user_id=user_id).first()
        
        if not prefs:
            # Create default preferences
            prefs = UserPreferences(user_id=user_id)
            db.session.add(prefs)
            db.session.commit()
        
        return jsonify(prefs.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@db_bp.route('/preferences/<user_id>', methods=['PUT'])
def update_preferences(user_id):
    """Update user preferences"""
    data = request.json
    
    try:
        prefs = UserPreferences.query.filter_by(user_id=user_id).first()
        
        if not prefs:
            prefs = UserPreferences(user_id=user_id)
            db.session.add(prefs)
        
        # Update fields
        if 'defaultReadingLevel' in data:
            prefs.default_reading_level = data['defaultReadingLevel']
        if 'textToSpeechEnabled' in data:
            prefs.text_to_speech_enabled = data['textToSpeechEnabled']
        if 'dyslexiaFontEnabled' in data:
            prefs.dyslexia_font_enabled = data['dyslexiaFontEnabled']
        if 'highContrastEnabled' in data:
            prefs.high_contrast_enabled = data['highContrastEnabled']
        if 'imageDescriptionsEnabled' in data:
            prefs.image_descriptions_enabled = data['imageDescriptionsEnabled']
        if 'theme' in data:
            prefs.theme = data['theme']
        if 'fontSize' in data:
            prefs.font_size = data['fontSize']
        
        prefs.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify(prefs.to_dict()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ==================== STATS ROUTES ====================

@db_bp.route('/stats/<user_id>', methods=['GET'])
def get_user_stats(user_id):
    """Get user statistics"""
    try:
        total_uploads = Upload.query.filter_by(user_id=user_id).count()
        total_saved = SavedContent.query.filter_by(user_id=user_id).count()
        
        # Recent uploads
        recent_uploads = Upload.query.filter_by(user_id=user_id).order_by(
            Upload.uploaded_at.desc()
        ).limit(5).all()
        
        # Recent saved content
        recent_saved = SavedContent.query.filter_by(user_id=user_id).order_by(
            SavedContent.saved_at.desc()
        ).limit(5).all()
        
        return jsonify({
            'totalUploads': total_uploads,
            'totalSaved': total_saved,
            'recentUploads': [upload.to_dict() for upload in recent_uploads],
            'recentSaved': [content.to_dict() for content in recent_saved]
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
