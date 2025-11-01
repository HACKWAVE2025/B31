"""
URL Content Processing Service
Extract content from web URLs
"""

import requests
from bs4 import BeautifulSoup
import html2text
from newspaper import Article

class URLProcessor:
    
    @staticmethod
    def extract_from_url(url):
        """Extract content from URL"""
        try:
            # Try newspaper3k first (best for articles)
            article = Article(url)
            article.download()
            article.parse()
            
            # Extract metadata
            title = article.title
            text = article.text
            authors = article.authors
            publish_date = article.publish_date
            top_image = article.top_image
            
            # Get HTML for additional parsing
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract images
            images = []
            for img in soup.find_all('img'):
                src = img.get('src', '')
                alt = img.get('alt', '')
                if src:
                    images.append({
                        'src': src,
                        'alt': alt,
                        'has_alt': bool(alt)
                    })
            
            # Extract links
            links = []
            for link in soup.find_all('a'):
                href = link.get('href', '')
                text = link.get_text(strip=True)
                if href:
                    links.append({
                        'href': href,
                        'text': text
                    })
            
            # Convert HTML to markdown
            h = html2text.HTML2Text()
            h.ignore_links = False
            h.ignore_images = False
            markdown_content = h.handle(response.text)
            
            return {
                'success': True,
                'url': url,
                'title': title,
                'text': text,
                'authors': authors,
                'publish_date': str(publish_date) if publish_date else None,
                'top_image': top_image,
                'images': images,
                'image_count': len(images),
                'links': links[:50],  # Limit links
                'link_count': len(links),
                'markdown': markdown_content,
                'word_count': len(text.split()),
                'accessibility_issues': URLProcessor._check_url_accessibility(images, links)
            }
        except Exception as e:
            # Fallback to basic scraping
            return URLProcessor._basic_url_extraction(url, str(e))
    
    @staticmethod
    def _basic_url_extraction(url, error=None):
        """Fallback URL extraction using BeautifulSoup"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title = soup.title.string if soup.title else 'Untitled'
            
            # Extract main text
            for script in soup(['script', 'style']):
                script.decompose()
            
            text = soup.get_text(separator='\n', strip=True)
            
            # Convert to markdown
            h = html2text.HTML2Text()
            markdown_content = h.handle(response.text)
            
            return {
                'success': True,
                'url': url,
                'title': title,
                'text': text,
                'markdown': markdown_content,
                'word_count': len(text.split()),
                'extraction_method': 'basic',
                'error': error
            }
        except Exception as e:
            return {
                'success': False,
                'url': url,
                'error': str(e)
            }
    
    @staticmethod
    def _check_url_accessibility(images, links):
        """Check URL content for accessibility issues"""
        issues = []
        
        # Check for images without ALT text
        images_without_alt = sum(1 for img in images if not img.get('has_alt'))
        if images_without_alt > 0:
            issues.append({
                'type': 'missing_alt_text',
                'severity': 'high',
                'count': images_without_alt,
                'message': f'{images_without_alt} images missing ALT text'
            })
        
        # Check for links without text
        links_without_text = sum(1 for link in links if not link.get('text'))
        if links_without_text > 0:
            issues.append({
                'type': 'empty_links',
                'severity': 'medium',
                'count': links_without_text,
                'message': f'{links_without_text} links without descriptive text'
            })
        
        return issues


# Singleton instance
url_processor = URLProcessor()
