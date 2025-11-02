"""
Accessibility Learning Hub - Flask Backend
Main application entry point
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from config import config
from models import db
import os

def create_app(config_name=None):
    """Application factory pattern"""
    
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Initialize CORS - Allow frontend on any localhost port
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173", "http://localhost:5174", "http://localhost:8080"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })
    
    # Initialize app directories
    config[config_name].init_app(app)
    
    # Create database tables and ensure survey columns exist
    with app.app_context():
        db.create_all()
        
        # Add survey columns if they don't exist
        try:
            from sqlalchemy import text, inspect
            inspector = inspect(db.engine)
            
            # Check if users table exists
            if 'users' in inspector.get_table_names():
                columns = [col['name'] for col in inspector.get_columns('users')]
                
                # Add survey_data column if missing
                if 'survey_data' not in columns:
                    print("⚠️  Adding survey_data column to users table...")
                    db.session.execute(text('ALTER TABLE users ADD COLUMN survey_data JSON'))
                    db.session.commit()
                    print("✅ survey_data column added")
                
                # Add survey_completed column if missing
                if 'survey_completed' not in columns:
                    print("⚠️  Adding survey_completed column to users table...")
                    db.session.execute(text('ALTER TABLE users ADD COLUMN survey_completed BOOLEAN DEFAULT FALSE'))
                    db.session.commit()
                    print("✅ survey_completed column added")
        except Exception as e:
            print(f"⚠️  Column migration error (may be normal on first run): {e}")
            db.session.rollback()
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.upload import upload_bp
    from routes.processing import processing_bp
    from routes.accessibility import accessibility_bp
    from routes.user import user_bp
    from routes.survey import survey_bp
    from routes.database import db_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(upload_bp, url_prefix='/api/upload')
    app.register_blueprint(processing_bp, url_prefix='/api/process')
    app.register_blueprint(accessibility_bp, url_prefix='/api/accessibility')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(survey_bp, url_prefix='/api/survey')
    app.register_blueprint(db_bp, url_prefix='/api/db')
    
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
