"""
Accessibility Learning Hub - Flask Backend
Main application entry point
"""

from flask import Flask, jsonify
from flask_cors import CORS
from config import config
import os

def create_app(config_name=None):
    """Application factory pattern"""
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173", "http://localhost:8080"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })
    
    # Initialize app directories
    config[config_name].init_app(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.upload import upload_bp
    from routes.processing import processing_bp
    from routes.accessibility import accessibility_bp
    from routes.user import user_bp
    from routes.survey import survey_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(upload_bp, url_prefix='/api/upload')
    app.register_blueprint(processing_bp, url_prefix='/api/process')
    app.register_blueprint(accessibility_bp, url_prefix='/api/accessibility')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(survey_bp, url_prefix='/api/survey')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(413)
    def file_too_large(error):
        return jsonify({'error': 'File too large. Maximum size is 50MB'}), 413
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Accessibility Learning Hub API',
            'version': '1.0.0'
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({
            'message': 'Welcome to Accessibility Learning Hub API',
            'version': '1.0.0',
            'documentation': '/api/docs',
            'health': '/api/health'
        }), 200
    
    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5001))  # Changed default port to 5001 to avoid macOS AirPlay conflict
    app.run(host='0.0.0.0', port=port, debug=True)
