"""
Processing Routes
Document processing, text extraction, parsing
"""

from flask import Blueprint, request, jsonify, current_app
from services.document_processor import DocumentProcessor
from routes.auth import token_required
import os

processing_bp = Blueprint('processing', __name__)


@processing_bp.route('/document', methods=['POST'])
@token_required
def process_document():
    """
    Process uploaded document and extract content
    
    Request Body:
    {
        "file_path": "/path/to/file",
        "file_type": "pdf",
        "user_id": "user123"
    }
    """
    try:
        data = request.get_json()
        file_path = data.get('file_path')
        file_type = data.get('file_type')
        user_id = data.get('user_id', request.user['uid'])
        
        if not file_path or not file_type:
            return jsonify({'error': 'file_path and file_type are required'}), 400
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        # Process document
        result = DocumentProcessor.process_document(file_path, file_type)
        
        # Get metadata
        metadata = DocumentProcessor.get_document_metadata(file_path)
        
        return jsonify({
            'success': True,
            'message': 'Document processed successfully',
            'content': result,
            'metadata': metadata,
            'user_id': user_id
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@processing_bp.route('/extract-text', methods=['POST'])
@token_required
def extract_text():
    """
    Extract raw text from document
    
    Request Body:
    {
        "file_path": "/path/to/file",
        "file_type": "pdf"
    }
    """
    try:
        data = request.get_json()
        file_path = data.get('file_path')
        file_type = data.get('file_type')
        
        if not file_path or not file_type:
            return jsonify({'error': 'file_path and file_type are required'}), 400
        
        result = DocumentProcessor.process_document(file_path, file_type)
        
        return jsonify({
            'success': True,
            'text': result.get('text', ''),
            'word_count': len(result.get('text', '').split()),
            'has_images': result.get('has_images', False),
            'has_tables': result.get('has_tables', False)
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@processing_bp.route('/batch-process', methods=['POST'])
@token_required
def batch_process():
    """
    Process multiple documents at once
    
    Request Body:
    {
        "files": [
            {"file_path": "/path/to/file1.pdf", "file_type": "pdf"},
            {"file_path": "/path/to/file2.docx", "file_type": "docx"}
        ]
    }
    """
    try:
        data = request.get_json()
        files = data.get('files', [])
        
        if not files:
            return jsonify({'error': 'No files provided'}), 400
        
        results = []
        errors = []
        
        for file_info in files:
            file_path = file_info.get('file_path')
            file_type = file_info.get('file_type')
            
            if not file_path or not file_type:
                errors.append({
                    'file': file_info,
                    'error': 'Missing file_path or file_type'
                })
                continue
            
            try:
                result = DocumentProcessor.process_document(file_path, file_type)
                results.append({
                    'file_path': file_path,
                    'file_type': file_type,
                    'content': result
                })
            except Exception as e:
                errors.append({
                    'file_path': file_path,
                    'error': str(e)
                })
        
        return jsonify({
            'success': True,
            'processed_count': len(results),
            'error_count': len(errors),
            'results': results,
            'errors': errors
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
