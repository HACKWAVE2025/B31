"""
User Routes
User profile, settings, history, saved content
"""

from flask import Blueprint, request, jsonify
from services.firebase_service import firebase_service
from routes.auth import token_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile', methods=['GET'])
@token_required
def get_profile():
    """
    Get user profile
    Requires authentication token
    """
    try:
        uid = request.user['uid']
        profile = firebase_service.get_user_profile(uid)
        
        if not profile:
            return jsonify({
                'success': False,
                'error': 'Profile not found'
            }), 404
        
        return jsonify({
            'success': True,
            'profile': profile
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/profile', methods=['PUT'])
@token_required
def update_profile():
    """
    Update user profile
    
    Request Body:
    {
        "display_name": "John Doe",
        "preferences": {
            "theme": "dark",
            "dyslexia_font": true,
            "high_contrast": false,
            "text_size": "large",
            "tts_voice": "en-US-Neural2-C",
            "tts_speed": 1.2
        },
        "accessibility_needs": ["dyslexia", "low_vision"]
    }
    """
    try:
        uid = request.user['uid']
        data = request.get_json()
        
        # Update profile
        firebase_service.update_user_profile(uid, data)
        
        return jsonify({
            'success': True,
            'message': 'Profile updated successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/preferences', methods=['GET'])
@token_required
def get_preferences():
    """Get user accessibility preferences"""
    try:
        uid = request.user['uid']
        profile = firebase_service.get_user_profile(uid)
        
        if not profile:
            return jsonify({
                'success': False,
                'error': 'Profile not found'
            }), 404
        
        return jsonify({
            'success': True,
            'preferences': profile.get('preferences', {})
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/preferences', methods=['PUT'])
@token_required
def update_preferences():
    """
    Update user preferences
    
    Request Body:
    {
        "theme": "dark",
        "dyslexia_font": true,
        "high_contrast": false,
        "text_size": "large",
        "tts_voice": "en-US-Neural2-C",
        "tts_speed": 1.2
    }
    """
    try:
        uid = request.user['uid']
        preferences = request.get_json()
        
        firebase_service.update_user_profile(uid, {'preferences': preferences})
        
        return jsonify({
            'success': True,
            'message': 'Preferences updated successfully',
            'preferences': preferences
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/history', methods=['GET'])
@token_required
def get_history():
    """
    Get user processing history
    
    Query Parameters:
    - limit: Number of items (default: 50)
    """
    try:
        uid = request.user['uid']
        limit = int(request.args.get('limit', 50))
        
        history = firebase_service.get_user_history(uid, limit)
        
        return jsonify({
            'success': True,
            'history': history,
            'count': len(history)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/history', methods=['POST'])
@token_required
def add_history():
    """
    Add item to user history
    
    Request Body:
    {
        "action": "document_processed",
        "file_name": "report.pdf",
        "adaptations_applied": ["simplify", "tts"],
        "metadata": {}
    }
    """
    try:
        uid = request.user['uid']
        history_item = request.get_json()
        
        firebase_service.save_user_history(uid, history_item)
        
        return jsonify({
            'success': True,
            'message': 'History item added successfully'
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/saved-content', methods=['GET'])
@token_required
def get_saved_content():
    """
    Get user's saved content
    
    Query Parameters:
    - limit: Number of items (default: 50)
    """
    try:
        uid = request.user['uid']
        limit = int(request.args.get('limit', 50))
        
        saved_content = firebase_service.get_saved_content(uid, limit)
        
        return jsonify({
            'success': True,
            'saved_content': saved_content,
            'count': len(saved_content)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/saved-content', methods=['POST'])
@token_required
def save_content():
    """
    Save generated content
    
    Request Body:
    {
        "title": "Simplified Research Article",
        "original_file": "research.pdf",
        "content_type": "simplified_text",
        "content": "...",
        "adaptations": ["simplify", "tts"],
        "metadata": {}
    }
    """
    try:
        uid = request.user['uid']
        content_data = request.get_json()
        
        content_id = firebase_service.save_content(uid, content_data)
        
        return jsonify({
            'success': True,
            'message': 'Content saved successfully',
            'content_id': content_id
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/accessibility-needs', methods=['GET'])
@token_required
def get_accessibility_needs():
    """Get user's declared accessibility needs"""
    try:
        uid = request.user['uid']
        profile = firebase_service.get_user_profile(uid)
        
        if not profile:
            return jsonify({
                'success': False,
                'error': 'Profile not found'
            }), 404
        
        return jsonify({
            'success': True,
            'accessibility_needs': profile.get('accessibility_needs', [])
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@user_bp.route('/accessibility-needs', methods=['PUT'])
@token_required
def update_accessibility_needs():
    """
    Update user's accessibility needs
    
    Request Body:
    {
        "accessibility_needs": ["dyslexia", "low_vision", "cognitive_disability"]
    }
    """
    try:
        uid = request.user['uid']
        data = request.get_json()
        accessibility_needs = data.get('accessibility_needs', [])
        
        firebase_service.update_user_profile(uid, {'accessibility_needs': accessibility_needs})
        
        return jsonify({
            'success': True,
            'message': 'Accessibility needs updated successfully',
            'accessibility_needs': accessibility_needs
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
