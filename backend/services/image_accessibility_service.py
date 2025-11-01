"""
Image Accessibility Service
Image analysis, ALT text generation, diagram description
"""

import os
import numpy as np
from PIL import Image

# Optional Google Cloud Vision
try:
    from google.cloud import vision
    VISION_AVAILABLE = True
except ImportError:
    VISION_AVAILABLE = False
    print("Warning: Google Cloud Vision not available. ALT text generation will use basic fallback.")

# Optional OpenCV
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    print("Warning: OpenCV not available. Some image analysis features will be limited.")

class ImageAccessibilityService:
    
    def __init__(self):
        self.vision_client = None
        self._init_vision_client()
    
    def _init_vision_client(self):
        """Initialize Google Cloud Vision API client"""
        try:
            from config import Config
            if VISION_AVAILABLE and Config.GOOGLE_APPLICATION_CREDENTIALS:
                self.vision_client = vision.ImageAnnotatorClient()
        except Exception as e:
            print(f"Google Vision API initialization warning: {e}")
    
    def generate_alt_text(self, image_path):
        """Generate ALT text for images using Google Cloud Vision"""
        try:
            if not self.vision_client:
                return self._generate_basic_alt_text(image_path)
            
            with open(image_path, 'rb') as image_file:
                content = image_file.read()
            
            image = vision.Image(content=content)
            
            # Detect labels
            labels_response = self.vision_client.label_detection(image=image)
            labels = [label.description for label in labels_response.label_annotations[:5]]
            
            # Detect objects
            objects_response = self.vision_client.object_localization(image=image)
            objects = [obj.name for obj in objects_response.localized_object_annotations[:5]]
            
            # Detect text
            text_response = self.vision_client.text_detection(image=image)
            detected_text = text_response.text_annotations[0].description if text_response.text_annotations else ""
            
            # Detect faces
            faces_response = self.vision_client.face_detection(image=image)
            face_count = len(faces_response.face_annotations)
            
            # Detect landmarks
            landmarks_response = self.vision_client.landmark_detection(image=image)
            landmarks = [landmark.description for landmark in landmarks_response.landmark_annotations[:3]]
            
            # Generate comprehensive ALT text
            alt_text = self._compose_alt_text(labels, objects, detected_text, face_count, landmarks)
            
            return {
                'alt_text': alt_text,
                'labels': labels,
                'objects': objects,
                'detected_text': detected_text[:200] if detected_text else None,
                'face_count': face_count,
                'landmarks': landmarks,
                'confidence': 'high'
            }
        except Exception as e:
            return self._generate_basic_alt_text(image_path, error=str(e))
    
    def _compose_alt_text(self, labels, objects, text, face_count, landmarks):
        """Compose descriptive ALT text from detected features"""
        parts = []
        
        if landmarks:
            parts.append(f"Image showing {', '.join(landmarks)}")
        elif objects:
            parts.append(f"Image containing {', '.join(objects[:3])}")
        elif labels:
            parts.append(f"Image depicting {', '.join(labels[:3])}")
        else:
            parts.append("Image")
        
        if face_count > 0:
            parts.append(f"with {face_count} person" + ("s" if face_count > 1 else ""))
        
        if text and len(text.strip()) > 0:
            text_preview = text.strip()[:100]
            parts.append(f"containing text: '{text_preview}'")
        
        return '. '.join(parts) + '.'
    
    def _generate_basic_alt_text(self, image_path, error=None):
        """Fallback ALT text generation using basic image analysis"""
        try:
            img = Image.open(image_path)
            
            # Get image properties
            width, height = img.size
            format_name = img.format
            mode = img.mode
            
            # Detect dominant colors
            img_array = np.array(img.resize((50, 50)))
            if len(img_array.shape) == 3:
                avg_color = np.mean(img_array, axis=(0, 1))
                dominant_color = self._get_color_name(avg_color)
            else:
                dominant_color = "grayscale"
            
            alt_text = f"{format_name} image ({width}x{height}) with predominant {dominant_color} tones"
            
            return {
                'alt_text': alt_text,
                'width': width,
                'height': height,
                'format': format_name,
                'dominant_color': dominant_color,
                'confidence': 'low',
                'error': error
            }
        except Exception as e:
            return {
                'alt_text': 'Image content could not be analyzed',
                'error': str(e)
            }
    
    def _get_color_name(self, rgb):
        """Convert RGB to color name"""
        r, g, b = rgb[:3]
        
        if r > 200 and g > 200 and b > 200:
            return "light"
        elif r < 50 and g < 50 and b < 50:
            return "dark"
        elif r > g and r > b:
            return "reddish"
        elif g > r and g > b:
            return "greenish"
        elif b > r and b > g:
            return "bluish"
        else:
            return "neutral"
    
    def describe_diagram(self, image_path, diagram_type='flowchart'):
        """
        Describe technical diagrams (flowcharts, molecular diagrams, etc.)
        for visually impaired users
        """
        try:
            # Use Vision API to detect shapes and text
            if self.vision_client:
                with open(image_path, 'rb') as image_file:
                    content = image_file.read()
                
                image = vision.Image(content=content)
                
                # Detect text for labels
                text_response = self.vision_client.text_detection(image=image)
                text_annotations = text_response.text_annotations
                
                # Detect objects/shapes
                objects_response = self.vision_client.object_localization(image=image)
                
                if diagram_type == 'flowchart':
                    return self._describe_flowchart(text_annotations, objects_response)
                elif diagram_type == 'molecular':
                    return self._describe_molecular_diagram(text_annotations, objects_response)
                else:
                    return self._describe_generic_diagram(text_annotations, objects_response)
            else:
                return {
                    'description': 'Diagram analysis requires Google Cloud Vision API',
                    'error': 'API not configured'
                }
        except Exception as e:
            return {
                'description': 'Error analyzing diagram',
                'error': str(e)
            }
    
    def _describe_flowchart(self, text_annotations, objects):
        """Generate text description of flowchart"""
        if not text_annotations:
            return {'description': 'Flowchart with unreadable elements'}
        
        # Extract text elements
        elements = [ann.description for ann in text_annotations[1:]]  # Skip first (full text)
        
        description = f"Flowchart containing {len(elements)} elements. "
        description += f"Process steps include: {', '.join(elements[:10])}"
        
        return {
            'description': description,
            'elements': elements,
            'element_count': len(elements),
            'type': 'flowchart'
        }
    
    def _describe_molecular_diagram(self, text_annotations, objects):
        """Generate text description of molecular diagram"""
        description = "Molecular structure diagram showing chemical compounds and bonds. "
        
        if text_annotations:
            labels = [ann.description for ann in text_annotations[1:]]
            description += f"Labeled elements: {', '.join(labels[:5])}"
        
        return {
            'description': description,
            'type': 'molecular_diagram'
        }
    
    def _describe_generic_diagram(self, text_annotations, objects):
        """Generate text description of generic diagram"""
        description = "Technical diagram "
        
        if text_annotations:
            labels = [ann.description for ann in text_annotations[1:]]
            description += f"with labeled components: {', '.join(labels[:10])}"
        
        return {
            'description': description,
            'type': 'generic_diagram'
        }
    
    def check_image_accessibility(self, image_path):
        """
        Comprehensive image accessibility check
        - Has ALT text
        - Sufficient contrast
        - Text readability
        """
        try:
            img = Image.open(image_path)
            
            # Generate ALT text
            alt_result = self.generate_alt_text(image_path)
            
            # Check if image contains text
            has_text = alt_result.get('detected_text') is not None
            
            # Basic contrast check (simplified)
            img_array = np.array(img.convert('L'))  # Convert to grayscale
            contrast = np.std(img_array)
            has_good_contrast = contrast > 50
            
            return {
                'image_path': image_path,
                'has_alt_text': True,
                'alt_text': alt_result['alt_text'],
                'has_detected_text': has_text,
                'detected_text': alt_result.get('detected_text'),
                'contrast_score': round(float(contrast), 2),
                'has_good_contrast': has_good_contrast,
                'accessibility_score': self._calculate_accessibility_score(
                    alt_result, has_text, has_good_contrast
                ),
                'recommendations': self._get_accessibility_recommendations(
                    alt_result, has_text, has_good_contrast
                )
            }
        except Exception as e:
            return {
                'error': str(e)
            }
    
    def _calculate_accessibility_score(self, alt_result, has_text, has_good_contrast):
        """Calculate overall accessibility score (0-100)"""
        score = 0
        
        # ALT text quality
        if alt_result.get('confidence') == 'high':
            score += 50
        else:
            score += 25
        
        # Contrast
        if has_good_contrast:
            score += 30
        else:
            score += 10
        
        # Text detection
        if has_text:
            score += 20
        
        return min(score, 100)
    
    def _get_accessibility_recommendations(self, alt_result, has_text, has_good_contrast):
        """Generate accessibility recommendations"""
        recommendations = []
        
        if alt_result.get('confidence') != 'high':
            recommendations.append("Consider adding manual ALT text for better description")
        
        if not has_good_contrast:
            recommendations.append("Increase image contrast for better visibility")
        
        if has_text:
            recommendations.append("Ensure text in image is also provided as actual text")
        
        if not recommendations:
            recommendations.append("Image meets basic accessibility standards")
        
        return recommendations


# Singleton instance
image_accessibility_service = ImageAccessibilityService()
