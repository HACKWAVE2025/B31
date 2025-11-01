"""
Authentication Routes
Handles Firebase authentication endpoints
"""

from flask import Blueprint, request, jsonify
from services.firebase_service import firebase_service
from functools import wraps

auth_bp = Blueprint('auth', __name__)


def token_required(f):
    """Decorator to require Firebase token"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        
        try:
            decoded_token = firebase_service.verify_token(token)
            request.user = decoded_token
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': 'Invalid token', 'message': str(e)}), 401
    
    return decorated


@auth_bp.route('/verify', methods=['POST'])
def verify_token():
    """
    Verify Firebase ID token
    
    Request Body:
    {
        "token": "firebase_id_token"
    }
    """
    try:
        data = request.get_json()
        token = data.get('token')
        
        if not token:
            return jsonify({'error': 'Token is required'}), 400
        
        decoded_token = firebase_service.verify_token(token)
        user_data = firebase_service.get_user(decoded_token['uid'])
        
        return jsonify({
            'success': True,
            'user': user_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 401


@auth_bp.route('/user/<uid>', methods=['GET'])
@token_required
def get_user(uid):
    """
    Get user details by UID
    Requires authentication token
    """
    try:
        # Verify user can only access their own data
        if request.user['uid'] != uid:
            return jsonify({'error': 'Unauthorized access'}), 403
        
        user_data = firebase_service.get_user(uid)
        profile_data = firebase_service.get_user_profile(uid)
        
        return jsonify({
            'success': True,
            'user': user_data,
            'profile': profile_data
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 404


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register new user (for backend use if needed)
    Note: Typically done through Firebase client SDK
    
    Request Body:
    {
        "email": "user@example.com",
        "password": "password123",
        "display_name": "John Doe"
    }
    """
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        display_name = data.get('display_name')
        
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        
        uid = firebase_service.create_user(email, password, display_name)
        
        return jsonify({
            'success': True,
            'uid': uid,
            'message': 'User created successfully'
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
