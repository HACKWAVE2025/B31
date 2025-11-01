import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class"""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    
    # Upload Configuration
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 50 * 1024 * 1024))  # 50MB
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt', 'png', 'jpg', 'jpeg', 'gif', 'pptx'}
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')
    FIREBASE_CONFIG = {
        'apiKey': os.getenv('FIREBASE_API_KEY'),
        'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
        'projectId': os.getenv('FIREBASE_PROJECT_ID'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.getenv('FIREBASE_APP_ID')
    }
    
    # Google Cloud
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    GOOGLE_CLOUD_PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
    
    # AWS
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://localhost:5173,http://localhost:8080').split(',')
    
    # Folders
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_DIR = os.path.join(BASE_DIR, UPLOAD_FOLDER)
    GENERATED_DIR = os.path.join(BASE_DIR, 'generated')
    TEMP_DIR = os.path.join(BASE_DIR, 'temp')
    
    @staticmethod
    def init_app(app):
        """Initialize application folders"""
        os.makedirs(Config.UPLOAD_DIR, exist_ok=True)
        os.makedirs(Config.GENERATED_DIR, exist_ok=True)
        os.makedirs(Config.TEMP_DIR, exist_ok=True)


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
