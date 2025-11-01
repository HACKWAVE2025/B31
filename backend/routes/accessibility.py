"""
Accessibility Routes
Text simplification, TTS, dyslexia formatting, image ALT text
"""

from flask import Blueprint, request, jsonify, current_app, send_file
from services.accessibility_service import accessibility_service
from services.tts_service import tts_service
from services.image_accessibility_service import image_accessibility_service
from routes.auth import token_required
import os
import uuid

accessibility_bp = Blueprint('accessibility', __name__)


@accessibility_bp.route('/simplify-text', methods=['POST'])
@token_required
def simplify_text():
    """
    Simplify text for cognitive accessibility
    
    Request Body:
    {
        "text": "Complex text to simplify...",
        "target_grade_level": 8
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        target_grade = data.get('target_grade_level', 8)
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        result = accessibility_service.simplify_text(text, target_grade)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/process-math', methods=['POST'])
@token_required
def process_math():
    """
    Process mathematical equations for accessibility
    
    Request Body:
    {
        "text": "Text containing $x^2 + y^2 = z^2$ equations"
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        result = accessibility_service.process_math_equations(text)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/dyslexia-format', methods=['POST'])
@token_required
def dyslexia_format():
    """
    Format text for dyslexia-friendly reading
    
    Request Body:
    {
        "text": "Text to format..."
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        result = accessibility_service.apply_dyslexia_friendly_format(text)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/check-contrast', methods=['POST'])
@token_required
def check_contrast():
    """
    Check color contrast for accessibility
    
    Request Body:
    {
        "foreground": "#000000",
        "background": "#FFFFFF"
    }
    """
    try:
        data = request.get_json()
        foreground = data.get('foreground')
        background = data.get('background')
        
        if not foreground or not background:
            return jsonify({'error': 'Both foreground and background colors are required'}), 400
        
        result = accessibility_service.adjust_color_contrast(foreground, background)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/extract-key-points', methods=['POST'])
@token_required
def extract_key_points():
    """
    Extract key points from text
    
    Request Body:
    {
        "text": "Long text...",
        "num_points": 5
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        num_points = data.get('num_points', 5)
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        result = accessibility_service.extract_key_points(text, num_points)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/describe-structure', methods=['POST'])
@token_required
def describe_structure():
    """
    Describe document structure for screen readers
    
    Request Body:
    {
        "text": "Document text with markdown..."
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        result = accessibility_service.describe_structure(text)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/text-to-speech', methods=['POST'])
@token_required
def text_to_speech():
    """
    Convert text to speech
    
    Request Body:
    {
        "text": "Text to convert to speech",
        "provider": "google",  // google, polly, gtts, pyttsx3
        "language": "en-US",
        "voice": "en-US-Neural2-C",
        "speaking_rate": 1.0
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        provider = data.get('provider', 'gtts')
        language = data.get('language', 'en-US')
        voice = data.get('voice', 'en-US-Neural2-C')
        speaking_rate = data.get('speaking_rate', 1.0)
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Generate unique filename
        filename = f"tts_{uuid.uuid4()}.mp3"
        output_path = os.path.join(current_app.config['GENERATED_DIR'], filename)
        
        # Generate speech
        if provider == 'google':
            result = tts_service.generate_speech(
                text, output_path, provider='google',
                language=language, voice_name=voice, speaking_rate=speaking_rate
            )
        elif provider == 'polly':
            result = tts_service.generate_speech(
                text, output_path, provider='polly',
                voice_id=voice, language_code=language
            )
        elif provider == 'gtts':
            result = tts_service.generate_speech(
                text, output_path, provider='gtts',
                language=language.split('-')[0]  # Extract base language
            )
        else:
            result = tts_service.generate_speech(text, output_path, provider='gtts')
        
        return jsonify({
            'success': True,
            'result': result,
            'download_url': f'/api/accessibility/download-audio/{filename}'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/download-audio/<filename>', methods=['GET'])
def download_audio(filename):
    """Download generated audio file"""
    try:
        file_path = os.path.join(current_app.config['GENERATED_DIR'], filename)
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@accessibility_bp.route('/available-voices', methods=['GET'])
@token_required
def get_available_voices():
    """
    Get available TTS voices
    
    Query Parameters:
    - provider: google, polly (optional)
    """
    try:
        provider = request.args.get('provider', 'google')
        voices = tts_service.get_available_voices(provider)
        
        return jsonify({
            'success': True,
            'provider': provider,
            'voices': voices
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/image/generate-alt', methods=['POST'])
@token_required
def generate_alt_text():
    """
    Generate ALT text for image
    
    Request Body:
    {
        "image_path": "/path/to/image.jpg"
    }
    """
    try:
        data = request.get_json()
        image_path = data.get('image_path')
        
        if not image_path:
            return jsonify({'error': 'image_path is required'}), 400
        
        if not os.path.exists(image_path):
            return jsonify({'error': 'Image not found'}), 404
        
        result = image_accessibility_service.generate_alt_text(image_path)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/image/describe-diagram', methods=['POST'])
@token_required
def describe_diagram():
    """
    Describe technical diagram
    
    Request Body:
    {
        "image_path": "/path/to/diagram.jpg",
        "diagram_type": "flowchart"  // flowchart, molecular, generic
    }
    """
    try:
        data = request.get_json()
        image_path = data.get('image_path')
        diagram_type = data.get('diagram_type', 'generic')
        
        if not image_path:
            return jsonify({'error': 'image_path is required'}), 400
        
        result = image_accessibility_service.describe_diagram(image_path, diagram_type)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/image/check-accessibility', methods=['POST'])
@token_required
def check_image_accessibility():
    """
    Comprehensive image accessibility check
    
    Request Body:
    {
        "image_path": "/path/to/image.jpg"
    }
    """
    try:
        data = request.get_json()
        image_path = data.get('image_path')
        
        if not image_path:
            return jsonify({'error': 'image_path is required'}), 400
        
        result = image_accessibility_service.check_image_accessibility(image_path)
        
        return jsonify({
            'success': True,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@accessibility_bp.route('/full-transformation', methods=['POST'])
@token_required
def full_transformation():
    """
    Apply comprehensive accessibility transformations
    
    Request Body:
    {
        "text": "Text content...",
        "adaptations": ["simplify", "dyslexia", "tts", "key_points"],
        "tts_provider": "gtts",
        "simplify_grade": 8
    }
    """
    try:
        data = request.get_json()
        text = data.get('text')
        adaptations = data.get('adaptations', [])
        tts_provider = data.get('tts_provider', 'gtts')
        simplify_grade = data.get('simplify_grade', 8)
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        results = {}
        
        # Text simplification
        if 'simplify' in adaptations:
            results['simplified'] = accessibility_service.simplify_text(text, simplify_grade)
        
        # Dyslexia formatting
        if 'dyslexia' in adaptations:
            results['dyslexia_formatted'] = accessibility_service.apply_dyslexia_friendly_format(text)
        
        # Key points extraction
        if 'key_points' in adaptations:
            results['key_points'] = accessibility_service.extract_key_points(text)
        
        # Structure description
        if 'structure' in adaptations:
            results['structure'] = accessibility_service.describe_structure(text)
        
        # Math processing
        if 'math' in adaptations:
            results['math_processed'] = accessibility_service.process_math_equations(text)
        
        # Text-to-speech
        if 'tts' in adaptations:
            filename = f"tts_{uuid.uuid4()}.mp3"
            output_path = os.path.join(current_app.config['GENERATED_DIR'], filename)
            tts_result = tts_service.generate_speech(text, output_path, provider=tts_provider)
            results['tts'] = {
                **tts_result,
                'download_url': f'/api/accessibility/download-audio/{filename}'
            }
        
        return jsonify({
            'success': True,
            'adaptations_applied': adaptations,
            'results': results
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
