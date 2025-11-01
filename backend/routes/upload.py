"""
Upload Routes
Handles file upload and URL processing
"""

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import validators
from services.url_processor import url_processor
from services.document_processor import DocumentProcessor
from routes.auth import token_required

upload_bp = Blueprint('upload', __name__)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@upload_bp.route('/document', methods=['POST'])
def upload_document():
    """
    Upload document for processing (no auth required for demo)
    
    Form Data:
    - file: The file to upload
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': 'File type not allowed',
                'allowed_types': list(current_app.config['ALLOWED_EXTENSIONS'])
            }), 400
        
        # Secure filename
        filename = secure_filename(file.filename)
        
        # Create upload directory
        upload_dir = current_app.config['UPLOAD_DIR']
        os.makedirs(upload_dir, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_dir, filename)
        file.save(file_path)
        
        # Get file info
        file_size = os.path.getsize(file_path)
        file_extension = filename.rsplit('.', 1)[1].lower()
        
        # Extract text content from the file using DocumentProcessor
        extracted_text = ''
        try:
            result = DocumentProcessor.process_document(file_path, file_extension)
            extracted_text = result.get('text', '')
            print(f"✅ Extracted {len(extracted_text)} characters from {filename}")
        except Exception as e:
            print(f"⚠️ Could not extract text from {filename}: {e}")
            extracted_text = ''
        
        return jsonify({
            'success': True,
            'message': 'File uploaded successfully',
            'file': {
                'id': filename,
                'filename': filename,
                'file_path': file_path,
                'file_size': file_size,
                'file_size_mb': round(file_size / (1024 * 1024), 2),
                'file_type': file_extension,
                'text_content': extracted_text,  # Include extracted text
                'word_count': len(extracted_text.split()) if extracted_text else 0
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@upload_bp.route('/file', methods=['POST'])
@token_required
def upload_file():
    """
    Upload file for processing
    
    Form Data:
    - file: The file to upload
    - user_id: User ID
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        user_id = request.form.get('user_id', request.user['uid'])
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': 'File type not allowed',
                'allowed_types': list(current_app.config['ALLOWED_EXTENSIONS'])
            }), 400
        
        # Secure filename
        filename = secure_filename(file.filename)
        
        # Create user-specific directory
        user_upload_dir = os.path.join(current_app.config['UPLOAD_DIR'], user_id)
        os.makedirs(user_upload_dir, exist_ok=True)
        
        # Save file
        file_path = os.path.join(user_upload_dir, filename)
        file.save(file_path)
        
        # Get file info
        file_size = os.path.getsize(file_path)
        file_extension = filename.rsplit('.', 1)[1].lower()
        
        return jsonify({
            'success': True,
            'message': 'File uploaded successfully',
            'file': {
                'filename': filename,
                'file_path': file_path,
                'file_size': file_size,
                'file_size_mb': round(file_size / (1024 * 1024), 2),
                'file_type': file_extension,
                'user_id': user_id
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@upload_bp.route('/url', methods=['POST'])
def process_url():
    """
    Process content from URL (no auth required for demo)
    
    Request Body:
    {
        "url": "https://example.com/article"
    }
    """
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Validate URL
        if not validators.url(url):
            return jsonify({'error': 'Invalid URL format'}), 400
        
        # Extract content
        result = url_processor.extract_from_url(url)
        
        if not result.get('success'):
            return jsonify({
                'success': False,
                'error': result.get('error', 'Failed to extract content from URL')
            }), 400
        
        # Save extracted content to file
        upload_dir = current_app.config['UPLOAD_DIR']
        os.makedirs(upload_dir, exist_ok=True)
        
        # Create filename from URL
        filename = f"url_content_{abs(hash(url))}.txt"
        file_path = os.path.join(upload_dir, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(result['text'])
        
        return jsonify({
            'success': True,
            'message': 'URL content extracted successfully',
            'content': result,
            'file': {
                'id': filename,
                'filename': filename,
                'file_path': file_path,
            }
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@upload_bp.route('/batch', methods=['POST'])
@token_required
def upload_batch():
    """
    Upload multiple files at once
    
    Form Data:
    - files[]: Multiple files
    - user_id: User ID
    """
    try:
        if 'files[]' not in request.files:
            return jsonify({'error': 'No files provided'}), 400
        
        files = request.files.getlist('files[]')
        user_id = request.form.get('user_id', request.user['uid'])
        
        uploaded_files = []
        errors = []
        
        for file in files:
            if file.filename == '':
                continue
            
            if not allowed_file(file.filename):
                errors.append({
                    'filename': file.filename,
                    'error': 'File type not allowed'
                })
                continue
            
            try:
                filename = secure_filename(file.filename)
                user_upload_dir = os.path.join(current_app.config['UPLOAD_DIR'], user_id)
                os.makedirs(user_upload_dir, exist_ok=True)
                
                file_path = os.path.join(user_upload_dir, filename)
                file.save(file_path)
                
                file_size = os.path.getsize(file_path)
                file_extension = filename.rsplit('.', 1)[1].lower()
                
                uploaded_files.append({
                    'filename': filename,
                    'file_path': file_path,
                    'file_size': file_size,
                    'file_type': file_extension
                })
            except Exception as e:
                errors.append({
                    'filename': file.filename,
                    'error': str(e)
                })
        
        return jsonify({
            'success': True,
            'message': f'{len(uploaded_files)} files uploaded successfully',
            'files': uploaded_files,
            'errors': errors,
            'user_id': user_id
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
