"""
Survey Routes
User survey, dynamic adaptation based on responses
"""

from flask import Blueprint, request, jsonify
from services.firebase_service import firebase_service
from routes.auth import token_required

survey_bp = Blueprint('survey', __name__)


# Survey questions template
SURVEY_QUESTIONS = [
    {
        "id": "q1",
        "question": "What are your primary accessibility needs?",
        "type": "multiple_choice",
        "options": [
            "Dyslexia support",
            "Visual impairment",
            "Cognitive disability",
            "Hearing impairment",
            "Motor disability",
            "None"
        ]
    },
    {
        "id": "q2",
        "question": "What type of content do you work with most?",
        "type": "multiple_choice",
        "options": [
            "Academic papers",
            "Technical documentation",
            "Books and literature",
            "News articles",
            "Educational materials",
            "Other"
        ]
    },
    {
        "id": "q3",
        "question": "What is your preferred reading level?",
        "type": "single_choice",
        "options": [
            "Elementary (Grade 3-5)",
            "Middle School (Grade 6-8)",
            "High School (Grade 9-12)",
            "College/Professional",
            "No preference"
        ]
    },
    {
        "id": "q4",
        "question": "Do you use screen readers?",
        "type": "boolean",
        "options": ["Yes", "No"]
    },
    {
        "id": "q5",
        "question": "What text-to-speech features do you need?",
        "type": "multiple_choice",
        "options": [
            "Standard text reading",
            "Math equation reading",
            "Table description",
            "Image description",
            "None"
        ]
    },
    {
        "id": "q6",
        "question": "What visual adaptations do you prefer?",
        "type": "multiple_choice",
        "options": [
            "Dyslexia-friendly fonts",
            "High contrast mode",
            "Larger text size",
            "Increased line spacing",
            "Color customization",
            "None"
        ]
    },
    {
        "id": "q7",
        "question": "How do you prefer complex diagrams to be handled?",
        "type": "single_choice",
        "options": [
            "Text description",
            "Simplified diagram",
            "Step-by-step breakdown",
            "Audio explanation",
            "All of the above"
        ]
    },
    {
        "id": "q8",
        "question": "What language do you primarily work in?",
        "type": "single_choice",
        "options": [
            "English",
            "Spanish",
            "French",
            "German",
            "Other"
        ]
    }
]


@survey_bp.route('/questions', methods=['GET'])
def get_survey_questions():
    """Get survey questions"""
    return jsonify({
        'success': True,
        'questions': SURVEY_QUESTIONS
    }), 200


@survey_bp.route('/submit', methods=['POST'])
@token_required
def submit_survey():
    """
    Submit survey responses
    
    Request Body:
    {
        "responses": {
            "q1": ["Dyslexia support", "Visual impairment"],
            "q2": ["Academic papers"],
            "q3": "High School (Grade 9-12)",
            "q4": "Yes",
            "q5": ["Standard text reading", "Math equation reading"],
            "q6": ["Dyslexia-friendly fonts", "High contrast mode"],
            "q7": "All of the above",
            "q8": "English"
        }
    }
    """
    try:
        uid = request.user['uid']
        data = request.get_json()
        responses = data.get('responses', {})
        
        # Generate adaptive recommendations based on responses
        recommendations = _generate_recommendations(responses)
        
        # Save survey responses to user profile
        firebase_service.update_user_profile(uid, {
            'survey_responses': responses,
            'survey_completed': True,
            'recommendations': recommendations
        })
        
        return jsonify({
            'success': True,
            'message': 'Survey submitted successfully',
            'recommendations': recommendations
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@survey_bp.route('/responses', methods=['GET'])
@token_required
def get_survey_responses():
    """Get user's survey responses"""
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
            'responses': profile.get('survey_responses', {}),
            'completed': profile.get('survey_completed', False),
            'recommendations': profile.get('recommendations', {})
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@survey_bp.route('/recommendations', methods=['GET'])
@token_required
def get_recommendations():
    """Get personalized recommendations based on survey"""
    try:
        uid = request.user['uid']
        profile = firebase_service.get_user_profile(uid)
        
        if not profile:
            return jsonify({
                'success': False,
                'error': 'Profile not found'
            }), 404
        
        responses = profile.get('survey_responses', {})
        recommendations = _generate_recommendations(responses)
        
        return jsonify({
            'success': True,
            'recommendations': recommendations
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def _generate_recommendations(responses):
    """Generate personalized recommendations based on survey responses"""
    recommendations = {
        'adaptations': [],
        'settings': {},
        'features': [],
        'priority': 'medium'
    }
    
    # Process Q1 - Accessibility needs
    accessibility_needs = responses.get('q1', [])
    if isinstance(accessibility_needs, str):
        accessibility_needs = [accessibility_needs]
    
    if 'Dyslexia support' in accessibility_needs:
        recommendations['adaptations'].extend(['dyslexia_font', 'text_spacing', 'simplify_text'])
        recommendations['settings']['dyslexia_font'] = True
        recommendations['settings']['font'] = 'OpenDyslexic'
        recommendations['features'].append('Dyslexia-friendly formatting')
    
    if 'Visual impairment' in accessibility_needs:
        recommendations['adaptations'].extend(['high_contrast', 'tts', 'screen_reader'])
        recommendations['settings']['high_contrast'] = True
        recommendations['settings']['text_size'] = 'large'
        recommendations['features'].append('Text-to-speech')
        recommendations['features'].append('High contrast mode')
    
    if 'Cognitive disability' in accessibility_needs:
        recommendations['adaptations'].extend(['simplify_text', 'key_points', 'structure_description'])
        recommendations['settings']['simplify_grade'] = 6
        recommendations['features'].append('Text simplification')
        recommendations['features'].append('Key points extraction')
    
    # Process Q3 - Reading level
    reading_level = responses.get('q3', '')
    if 'Elementary' in reading_level:
        recommendations['settings']['target_grade'] = 4
    elif 'Middle School' in reading_level:
        recommendations['settings']['target_grade'] = 7
    elif 'High School' in reading_level:
        recommendations['settings']['target_grade'] = 10
    else:
        recommendations['settings']['target_grade'] = 12
    
    # Process Q4 - Screen reader
    if responses.get('q4') == 'Yes':
        recommendations['adaptations'].append('screen_reader_optimized')
        recommendations['features'].append('Screen reader optimization')
        recommendations['settings']['alt_text_generation'] = True
    
    # Process Q5 - TTS features
    tts_needs = responses.get('q5', [])
    if isinstance(tts_needs, str):
        tts_needs = [tts_needs]
    
    if 'Math equation reading' in tts_needs:
        recommendations['adaptations'].append('math_to_speech')
        recommendations['features'].append('Mathematical equation narration')
    
    if 'Image description' in tts_needs:
        recommendations['adaptations'].append('image_description')
        recommendations['features'].append('Automatic image descriptions')
    
    # Process Q6 - Visual adaptations
    visual_prefs = responses.get('q6', [])
    if isinstance(visual_prefs, str):
        visual_prefs = [visual_prefs]
    
    if 'Dyslexia-friendly fonts' in visual_prefs:
        recommendations['settings']['font'] = 'OpenDyslexic'
    
    if 'High contrast mode' in visual_prefs:
        recommendations['settings']['theme'] = 'high_contrast'
    
    if 'Larger text size' in visual_prefs:
        recommendations['settings']['text_size'] = 'x-large'
    
    if 'Increased line spacing' in visual_prefs:
        recommendations['settings']['line_height'] = 2.0
    
    # Process Q7 - Diagram handling
    diagram_pref = responses.get('q7', '')
    if 'Text description' in diagram_pref or 'All of the above' in diagram_pref:
        recommendations['adaptations'].append('diagram_to_text')
        recommendations['features'].append('Diagram text descriptions')
    
    # Process Q8 - Language
    language = responses.get('q8', 'English')
    language_codes = {
        'English': 'en-US',
        'Spanish': 'es-ES',
        'French': 'fr-FR',
        'German': 'de-DE'
    }
    recommendations['settings']['language'] = language_codes.get(language, 'en-US')
    
    # Determine priority based on needs
    if len(accessibility_needs) > 2:
        recommendations['priority'] = 'high'
    elif len(accessibility_needs) > 0:
        recommendations['priority'] = 'medium'
    else:
        recommendations['priority'] = 'low'
    
    # Remove duplicates
    recommendations['adaptations'] = list(set(recommendations['adaptations']))
    recommendations['features'] = list(set(recommendations['features']))
    
    return recommendations
