"""
Text-to-Speech Service
Integrates Google Cloud TTS, Amazon Polly, and gTTS
"""

import os
from gtts import gTTS

# Optional cloud providers
try:
    import boto3
    BOTO3_AVAILABLE = True
except ImportError:
    BOTO3_AVAILABLE = False
    print("Warning: boto3 not available. Amazon Polly TTS will be disabled.")

try:
    from google.cloud import texttospeech
    GOOGLE_TTS_AVAILABLE = True
except ImportError:
    GOOGLE_TTS_AVAILABLE = False
    print("Warning: Google Cloud TTS not available. Will use fallback providers.")

try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False
    print("Warning: pyttsx3 not available. Offline TTS will be disabled.")

from config import Config

class TTSService:
    
    def __init__(self):
        self.google_client = None
        self.polly_client = None
        self._init_clients()
    
    def _init_clients(self):
        """Initialize TTS clients"""
        # Google Cloud TTS
        try:
            if GOOGLE_TTS_AVAILABLE and Config.GOOGLE_APPLICATION_CREDENTIALS:
                self.google_client = texttospeech.TextToSpeechClient()
        except Exception as e:
            print(f"Google TTS initialization warning: {e}")
        
        # Amazon Polly
        try:
            if BOTO3_AVAILABLE and Config.AWS_ACCESS_KEY_ID:
                self.polly_client = boto3.client(
                    'polly',
                    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
                    region_name=Config.AWS_REGION
                )
        except Exception as e:
            print(f"Amazon Polly initialization warning: {e}")
    
    def google_tts(self, text, output_path, language='en-US', voice_name='en-US-Neural2-C', speaking_rate=1.0):
        """Generate speech using Google Cloud TTS"""
        try:
            if not self.google_client:
                raise ValueError("Google TTS client not initialized")
            
            synthesis_input = texttospeech.SynthesisInput(text=text)
            
            voice = texttospeech.VoiceSelectionParams(
                language_code=language,
                name=voice_name
            )
            
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=speaking_rate,
                pitch=0.0
            )
            
            response = self.google_client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            with open(output_path, 'wb') as out:
                out.write(response.audio_content)
            
            return {
                'success': True,
                'file_path': output_path,
                'provider': 'google',
                'voice': voice_name,
                'language': language
            }
        except Exception as e:
            raise ValueError(f"Google TTS error: {str(e)}")
    
    def amazon_polly_tts(self, text, output_path, voice_id='Joanna', language_code='en-US', engine='neural'):
        """Generate speech using Amazon Polly"""
        try:
            if not self.polly_client:
                raise ValueError("Amazon Polly client not initialized")
            
            response = self.polly_client.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId=voice_id,
                LanguageCode=language_code,
                Engine=engine
            )
            
            with open(output_path, 'wb') as file:
                file.write(response['AudioStream'].read())
            
            return {
                'success': True,
                'file_path': output_path,
                'provider': 'amazon_polly',
                'voice': voice_id,
                'language': language_code
            }
        except Exception as e:
            raise ValueError(f"Amazon Polly error: {str(e)}")
    
    def gtts_generate(self, text, output_path, language='en', slow=False):
        """Generate speech using gTTS (free alternative)"""
        try:
            tts = gTTS(text=text, lang=language, slow=slow)
            tts.save(output_path)
            
            return {
                'success': True,
                'file_path': output_path,
                'provider': 'gtts',
                'language': language
            }
        except Exception as e:
            raise ValueError(f"gTTS error: {str(e)}")
    
    def pyttsx3_generate(self, text, output_path, rate=150, volume=1.0):
        """Generate speech using pyttsx3 (offline)"""
        if not PYTTSX3_AVAILABLE:
            raise ValueError("pyttsx3 not available. Install it for offline TTS support.")
        
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)
            
            engine.save_to_file(text, output_path)
            engine.runAndWait()
            
            return {
                'success': True,
                'file_path': output_path,
                'provider': 'pyttsx3'
            }
        except Exception as e:
            raise ValueError(f"pyttsx3 error: {str(e)}")
    
    def generate_speech(self, text, output_path, provider='google', **kwargs):
        """Main TTS generation method with fallback"""
        
        # Chunk large text
        if len(text) > 5000:
            chunks = self._chunk_text(text, 5000)
        else:
            chunks = [text]
        
        results = []
        
        for i, chunk in enumerate(chunks):
            chunk_path = output_path if len(chunks) == 1 else output_path.replace('.mp3', f'_part{i+1}.mp3')
            
            try:
                if provider == 'google' and self.google_client:
                    result = self.google_tts(chunk, chunk_path, **kwargs)
                elif provider == 'polly' and self.polly_client:
                    result = self.amazon_polly_tts(chunk, chunk_path, **kwargs)
                elif provider == 'gtts':
                    result = self.gtts_generate(chunk, chunk_path, **kwargs)
                elif provider == 'pyttsx3':
                    result = self.pyttsx3_generate(chunk, chunk_path, **kwargs)
                else:
                    # Fallback to gTTS
                    result = self.gtts_generate(chunk, chunk_path)
                
                results.append(result)
            except Exception as e:
                # Fallback to gTTS
                try:
                    result = self.gtts_generate(chunk, chunk_path)
                    results.append(result)
                except:
                    raise ValueError(f"All TTS providers failed: {str(e)}")
        
        return {
            'success': True,
            'files': results,
            'chunk_count': len(chunks)
        }
    
    def _chunk_text(self, text, max_length):
        """Split text into chunks for TTS"""
        sentences = text.split('. ')
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < max_length:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def get_available_voices(self, provider='google'):
        """Get available voices for a provider"""
        try:
            if provider == 'google' and self.google_client:
                voices = self.google_client.list_voices()
                return [
                    {
                        'name': voice.name,
                        'language': voice.language_codes[0],
                        'gender': texttospeech.SsmlVoiceGender(voice.ssml_gender).name
                    }
                    for voice in voices.voices
                ]
            elif provider == 'polly' and self.polly_client:
                response = self.polly_client.describe_voices()
                return [
                    {
                        'name': voice['Id'],
                        'language': voice['LanguageCode'],
                        'gender': voice['Gender']
                    }
                    for voice in response['Voices']
                ]
            else:
                return []
        except Exception as e:
            return []


# Singleton instance
tts_service = TTSService()
