import json
from kivy.network.urlrequest import UrlRequest
from kivy.logger import Logger

class APIClient:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        """Load API configuration"""
        try:
            with open('config.json') as f:
                self.config = json.load(f)
            self.base_url = self.config['api']['base_url']
        except Exception as e:
            Logger.error(f'APIClient: Config load failed - {e}')
            self.base_url = "https://web-production-ac2e5.up.railway.app/api"
    
    def get_video_info(self, url, success_callback, error_callback=None):
        """Fetch video information from backend"""
        endpoint = f"{self.base_url}{self.config['api']['endpoints']['video_info']}"
        
        Logger.info(f'APIClient: Fetching info for URL - {url}')
        
        def on_success(request, result):
            Logger.info('APIClient: Video info fetched successfully')
            success_callback(result)
        
        def on_error(request, error):
            error_msg = f"API Error: {error}"
            Logger.error(f'APIClient: {error_msg}')
            if error_callback:
                error_callback(error_msg)
        
        UrlRequest(
            endpoint,
            req_headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            req_body=json.dumps({'url': url}),
            on_success=on_success,
            on_failure=on_error,
            on_error=on_error
        )
    
    def get_download_url(self, url, format_id, success_callback, error_callback=None):
        """Get download URL from backend"""
        endpoint = f"{self.base_url}{self.config['api']['endpoints']['download']}"
        
        Logger.info(f'APIClient: Getting download URL for format {format_id}')
        
        def on_success(request, result):
            Logger.info('APIClient: Download URL received')
            success_callback(result)
        
        def on_error(request, error):
            error_msg = f"Download API Error: {error}"
            Logger.error(f'APIClient: {error_msg}')
            if error_callback:
                error_callback(error_msg)
        
        UrlRequest(
            endpoint,
            req_headers={'Content-Type': 'application/json'},
            req_body=json.dumps({
                'url': url,
                'format_id': format_id
            }),
            on_success=on_success,
            on_failure=on_error,
            on_error=on_error
        )
