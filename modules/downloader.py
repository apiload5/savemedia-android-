import os
import json
from kivy import platform
from kivy.logger import Logger
from kivy.clock import Clock

class DownloadManager:
    def __init__(self):
        self.download_folder = self.get_download_folder()
        self.load_config()
    
    def load_config(self):
        """Load app configuration"""
        try:
            with open('config.json') as f:
                self.config = json.load(f)
        except:
            self.config = {"app": {"download_folder": "Savemedia"}}
    
    def get_download_folder(self):
        """Get appropriate download folder based on platform"""
        try:
            if platform == 'android':
                from android.storage import primary_external_storage_path
                base_dir = primary_external_storage_path()
                download_dir = os.path.join(base_dir, 'Download', 'Savemedia')
            else:
                # For desktop testing
                download_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'Savemedia')
            
            os.makedirs(download_dir, exist_ok=True)
            Logger.info(f'DownloadManager: Download folder - {download_dir}')
            return download_dir
            
        except Exception as e:
            Logger.error(f'DownloadManager: Folder setup failed - {e}')
            return './downloads'
    
    def download_video(self, download_url, filename, callback):
        """Download video file"""
        try:
            from kivy.network.urlrequest import UrlRequest
            
            # Ensure filename has proper extension
            if not filename.lower().endswith(('.mp4', '.mp3', '.webm')):
                filename += '.mp4'
            
            filepath = os.path.join(self.download_folder, filename)
            
            def on_success(request, result):
                try:
                    with open(filepath, 'wb') as f:
                        f.write(result)
                    
                    # Save to history
                    self.save_to_history({
                        'title': filename,
                        'file_path': filepath,
                        'url': download_url
                    })
                    
                    Logger.info(f'DownloadManager: Download successful - {filepath}')
                    callback(True, filepath)
                    
                except Exception as e:
                    Logger.error(f'DownloadManager: File save failed - {e}')
                    callback(False, str(e))
            
            def on_error(request, error):
                error_msg = f"Download failed: {error}"
                Logger.error(f'DownloadManager: {error_msg}')
                callback(False, error_msg)
            
            def on_progress(request, current_size, total_size):
                if total_size:
                    percent = (current_size / total_size) * 100
                    Logger.info(f'DownloadManager: Progress - {percent:.1f}%')
            
            Logger.info(f'DownloadManager: Starting download - {filename}')
            
            UrlRequest(
                download_url,
                on_success=on_success,
                on_error=on_error,
                on_progress=on_progress,
                chunk_size=8192,  # 8KB chunks
                timeout=30
            )
            
        except Exception as e:
            Logger.error(f'DownloadManager: Download setup failed - {e}')
            callback(False, str(e))
    
    def save_to_history(self, video_data):
        """Save download to history"""
        try:
            history_file = os.path.join('data', 'download_history.json')
            os.makedirs('data', exist_ok=True)
            
            try:
                with open(history_file, 'r') as f:
                    history = json.load(f)
            except:
                history = []
            
            history.insert(0, {
                'title': video_data.get('title', 'Unknown'),
                'url': video_data.get('url', ''),
                'file_path': video_data.get('file_path', ''),
                'date': self.get_current_date()
            })
            
            # Keep only last 20 downloads
            history = history[:20]
            
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
            
            Logger.info('DownloadManager: Saved to history')
            
        except Exception as e:
            Logger.error(f'DownloadManager: History save failed - {e}')
    
    def get_current_date(self):
        """Get current date string"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def get_download_history(self):
        """Get download history"""
        try:
            history_file = os.path.join('data', 'download_history.json')
            with open(history_file, 'r') as f:
                return json.load(f)
        except:
            return []
