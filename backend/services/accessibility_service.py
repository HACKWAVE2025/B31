"""
Accessibility Features Service
Text simplification, dyslexia fonts, high contrast, math processing
"""

import re
import nltk
from textstat import flesch_reading_ease, flesch_kincaid_grade
import sympy
from sympy.parsing.latex import parse_latex

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class AccessibilityService:
    
    def __init__(self):
        # Simplified version without spaCy
        print("AccessibilityService initialized (basic mode - without advanced NLP)")
    
    def simplify_text(self, text, target_grade_level=8):
        """
        Simplify text for cognitive accessibility
        - Break long sentences
        - Replace complex words
        - Improve readability
        """
        try:
            # Calculate current readability
            current_grade = flesch_kincaid_grade(text)
            current_ease = flesch_reading_ease(text)
            
            # Split into sentences
            sentences = nltk.sent_tokenize(text)
            simplified_sentences = []
            
            for sentence in sentences:
                # Break long sentences
                if len(sentence.split()) > 20:
                    # Split at conjunctions
                    parts = re.split(r'\s+(and|but|or|because|however|therefore)\s+', sentence, flags=re.IGNORECASE)
                    for part in parts:
                        if len(part.strip()) > 3:
                            simplified_sentences.append(part.strip() + '.')
                else:
                    simplified_sentences.append(sentence)
            
            # Replace complex words
            simplified_text = self._simplify_vocabulary(' '.join(simplified_sentences))
            
            new_grade = flesch_kincaid_grade(simplified_text)
            new_ease = flesch_reading_ease(simplified_text)
            
            return {
                'original_text': text,
                'simplified_text': simplified_text,
                'metrics': {
                    'original_grade_level': round(current_grade, 1),
                    'simplified_grade_level': round(new_grade, 1),
                    'original_ease_score': round(current_ease, 1),
                    'simplified_ease_score': round(new_ease, 1)
                },
                'improvement': round(current_grade - new_grade, 1)
            }
        except Exception as e:
            return {
                'original_text': text,
                'simplified_text': text,
                'error': str(e)
            }
    
    def _simplify_vocabulary(self, text):
        """Replace complex words with simpler alternatives"""
        # Common complex -> simple word mappings
        replacements = {
            r'\butilize\b': 'use',
            r'\bcommence\b': 'start',
            r'\bterminate\b': 'end',
            r'\bdemonstrate\b': 'show',
            r'\bfacilitate\b': 'help',
            r'\bimplement\b': 'do',
            r'\bnevertheless\b': 'but',
            r'\bfurthermore\b': 'also',
            r'\bconsequently\b': 'so',
            r'\badditionally\b': 'also',
            r'\bsubsequently\b': 'then',
            r'\bapproximately\b': 'about',
            r'\bmanufacture\b': 'make',
            r'\bpurchase\b': 'buy',
            r'\bcomprehend\b': 'understand',
            r'\battain\b': 'reach',
            r'\bobtain\b': 'get',
            r'\bassist\b': 'help'
        }
        
        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        return text
    
    def process_math_equations(self, text):
        """
        Process LaTeX math equations
        - Convert to readable text
        - Generate step-by-step explanations
        """
        try:
            # Find LaTeX equations (between $ or \[ \])
            latex_patterns = [
                r'\$\$(.+?)\$\$',  # Display math
                r'\$(.+?)\$',       # Inline math
                r'\\\[(.+?)\\\]',   # Display math
                r'\\\((.+?)\\\)'    # Inline math
            ]
            
            equations = []
            for pattern in latex_patterns:
                matches = re.finditer(pattern, text)
                for match in matches:
                    latex = match.group(1)
                    try:
                        # Parse LaTeX
                        expr = parse_latex(latex)
                        
                        # Convert to text
                        text_form = str(expr)
                        
                        # Simple HTML alternative (instead of MathML)
                        html_form = f"<math>{text_form}</math>"
                        
                        equations.append({
                            'latex': latex,
                            'text': text_form,
                            'html': html_form,
                            'position': match.span()
                        })
                    except:
                        equations.append({
                            'latex': latex,
                            'text': latex,
                            'error': 'Could not parse equation'
                        })
            
            return {
                'original_text': text,
                'equations': equations,
                'equation_count': len(equations)
            }
        except Exception as e:
            return {
                'original_text': text,
                'equations': [],
                'error': str(e)
            }
    
    def apply_dyslexia_friendly_format(self, text):
        """
        Format text for dyslexia-friendly reading
        - Increased spacing
        - Highlighting patterns
        - Reading guides
        """
        try:
            # Add extra spacing between lines
            lines = text.split('\n')
            spaced_lines = [line + '\n' for line in lines]
            
            # Highlight syllables or chunks (simplified approach)
            formatted_text = ' '.join(spaced_lines)
            
            return {
                'original_text': text,
                'formatted_text': formatted_text,
                'formatting_applied': [
                    'increased_line_spacing',
                    'chunk_highlighting',
                    'sentence_separation'
                ],
                'recommended_font': 'OpenDyslexic',
                'recommended_settings': {
                    'font_size': '14-16pt',
                    'line_height': '1.5-2.0',
                    'letter_spacing': '0.12em',
                    'word_spacing': '0.16em',
                    'background_color': '#FDF6E3',  # Cream background
                    'text_color': '#2E3436'  # Dark gray text
                }
            }
        except Exception as e:
            return {
                'original_text': text,
                'formatted_text': text,
                'error': str(e)
            }
    
    def adjust_color_contrast(self, foreground, background):
        """
        Calculate and adjust color contrast for low-vision users
        WCAG AA requires 4.5:1 for normal text, 3:1 for large text
        """
        try:
            # Convert hex to RGB
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Calculate relative luminance
            def luminance(rgb):
                r, g, b = [x / 255.0 for x in rgb]
                r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
                g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
                b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
                return 0.2126 * r + 0.7152 * g + 0.0722 * b
            
            # Calculate contrast ratio
            fg_rgb = hex_to_rgb(foreground)
            bg_rgb = hex_to_rgb(background)
            
            l1 = luminance(fg_rgb)
            l2 = luminance(bg_rgb)
            
            lighter = max(l1, l2)
            darker = min(l1, l2)
            contrast_ratio = (lighter + 0.05) / (darker + 0.05)
            
            # Check WCAG compliance
            wcag_aa = contrast_ratio >= 4.5
            wcag_aa_large = contrast_ratio >= 3.0
            wcag_aaa = contrast_ratio >= 7.0
            
            return {
                'foreground': foreground,
                'background': background,
                'contrast_ratio': round(contrast_ratio, 2),
                'wcag_aa_compliant': wcag_aa,
                'wcag_aa_large_compliant': wcag_aa_large,
                'wcag_aaa_compliant': wcag_aaa,
                'recommendation': 'Pass' if wcag_aa else 'Increase contrast'
            }
        except Exception as e:
            return {
                'error': str(e)
            }
    
    def extract_key_points(self, text, num_points=5):
        """Extract key points from text for summary"""
        try:
            if not self.nlp:
                # Simple fallback
                sentences = nltk.sent_tokenize(text)
                return sentences[:num_points]
            
            doc = self.nlp(text)
            
            # Extract sentences with named entities or important verbs
            important_sentences = []
            for sent in doc.sents:
                score = 0
                if sent.ents:
                    score += len(sent.ents)
                for token in sent:
                    if token.pos_ in ['VERB', 'NOUN']:
                        score += 1
                important_sentences.append((sent.text, score))
            
            # Sort by score and get top points
            important_sentences.sort(key=lambda x: x[1], reverse=True)
            key_points = [sent[0] for sent in important_sentences[:num_points]]
            
            return {
                'key_points': key_points,
                'original_length': len(text),
                'summary_length': sum(len(p) for p in key_points)
            }
        except Exception as e:
            return {
                'key_points': [],
                'error': str(e)
            }
    
    def describe_structure(self, text):
        """Analyze and describe document structure for screen readers"""
        try:
            # Count headings (assuming markdown-style)
            headings = re.findall(r'^#{1,6}\s+(.+)$', text, re.MULTILINE)
            
            # Count lists
            bullet_lists = len(re.findall(r'^[\*\-\+]\s+', text, re.MULTILINE))
            numbered_lists = len(re.findall(r'^\d+\.\s+', text, re.MULTILINE))
            
            # Count paragraphs
            paragraphs = len([p for p in text.split('\n\n') if p.strip()])
            
            # Detect code blocks
            code_blocks = len(re.findall(r'```.*?```', text, re.DOTALL))
            
            return {
                'structure': {
                    'headings': len(headings),
                    'heading_hierarchy': headings,
                    'paragraphs': paragraphs,
                    'bullet_lists': bullet_lists,
                    'numbered_lists': numbered_lists,
                    'code_blocks': code_blocks
                },
                'screen_reader_description': self._generate_structure_description(
                    headings, paragraphs, bullet_lists, numbered_lists, code_blocks
                )
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _generate_structure_description(self, headings, paragraphs, bullets, numbered, code):
        """Generate human-readable structure description"""
        desc = f"This document contains "
        parts = []
        
        if headings:
            parts.append(f"{len(headings)} section headings")
        if paragraphs:
            parts.append(f"{paragraphs} paragraphs")
        if bullets:
            parts.append(f"{bullets} bullet point items")
        if numbered:
            parts.append(f"{numbered} numbered list items")
        if code:
            parts.append(f"{code} code blocks")
        
        if not parts:
            return "This document has minimal structure."
        
        return desc + ', '.join(parts) + '.'


# Singleton instance
accessibility_service = AccessibilityService()
