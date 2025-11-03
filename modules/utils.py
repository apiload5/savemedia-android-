import re
from kivy.logger import Logger

class Utils:
    @staticmethod
    def is_valid_url(url):
        """Check if URL is valid"""
        if not url or not isinstance(url, str):
            return False
        
        url_pattern = re.compile(
            r'^(https?://)?'  # http:// or https://
            r'(([A-Z0-9]([A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        return bool(url_pattern.match(url))
    
    @staticmethod
    def extract_video_id(url):
        """Extract video ID from common platforms"""
        try:
            # YouTube
            if 'youtube.com/watch?v=' in url:
                return url.split('v=')[1].split('&')[0]
            elif 'youtu.be/' in url:
                return url.split('youtu.be/')[1].split('?')[0]
            
            # Other platforms can be added here
            return None
        except:
            return None
    
    @staticmethod
    def format_file_size(size_bytes):
        """Format file size in human readable format"""
        if not size_bytes:
            return "Unknown"
        
        try:
            size_bytes = int(size_bytes)
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size_bytes < 1024.0:
                    return f"{size_bytes:.1f} {unit}"
                size_bytes /= 1024.0
            return f"{size_bytes:.1f} TB"
        except:
            return "Unknown"
    
    @staticmethod
    def sanitize_filename(filename):
        """Remove invalid characters from filename"""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename[:100]  # Limit length

# Create utility instance
utils = Utils()
