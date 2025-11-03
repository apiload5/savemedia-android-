from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

# Set window size for mobile preview
if platform != 'android':
    Window.size = (360, 640)

Builder.load_file('savemedia.kv')

class HomeScreen(Screen):
    def fetch_video_info(self):
        url = self.ids.url_input.text.strip()
        if not url:
            self.show_error("Please enter a video URL")
            return
        
        self.show_processing()
        Clock.schedule_once(self.mock_video_data, 2)
    
    def mock_video_data(self, dt):
        self.hide_processing()
        self.manager.current = 'result'
        result_screen = self.manager.get_screen('result')
        result_screen.display_video_info({
            "title": "Sample YouTube Video",
            "duration": "5:30",
            "uploader": "Sample Channel", 
            "view_count": "1.2M",
            "thumbnail": "https://via.placeholder.com/200x120/667eea/white?text=Thumbnail",
            "formats": [
                {"quality": "1080p", "format": "MP4", "size": "125MB", "format_id": "137"},
                {"quality": "720p", "format": "MP4", "size": "85MB", "format_id": "136"},
                {"quality": "480p", "format": "MP4", "size": "45MB", "format_id": "135"},
                {"quality": "MP3 Audio", "format": "MP3", "size": "8MB", "format_id": "140"}
            ]
        })
    
    def show_processing(self):
        self.ids.processing_container.opacity = 1
    
    def hide_processing(self):
        self.ids.processing_container.opacity = 0
    
    def show_error(self, message):
        self.ids.error_container.text = message
        self.ids.error_container.opacity = 1
        Clock.schedule_once(self.hide_error, 3)
    
    def hide_error(self, dt):
        self.ids.error_container.opacity = 0

class ResultScreen(Screen):
    def display_video_info(self, data):
        self.ids.video_title.text = data['title']
        self.ids.video_duration.text = f"Duration: {data['duration']}"
        self.ids.video_uploader.text = f"Uploader: {data['uploader']}"
        self.ids.video_views.text = f"Views: {data['view_count']}"
        
        self.ids.formats_grid.clear_widgets()
        
        for fmt in data['formats']:
            from kivy.uix.button import Button
            btn = Button(
                text=f"{fmt['quality']} ({fmt['format']}) - {fmt['size']}",
                size_hint_y=None,
                height='45dp',
                background_color=(0.129, 0.588, 0.953, 1),
                background_normal='',
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda x, f=fmt: self.select_format(f))
            self.ids.formats_grid.add_widget(btn)
    
    def select_format(self, format_data):
        self.manager.current = 'download'
        download_screen = self.manager.get_screen('download')
        download_screen.set_download_data(format_data)

class DownloadScreen(Screen):
    def set_download_data(self, format_data):
        self.selected_format = format_data
        self.ids.preview_title.text = f"{format_data['quality']} {format_data['format']}"
    
    def start_download(self):
        app = App.get_running_app()
        Clock.schedule_once(self.process_download, 3)
    
    def process_download(self, dt):
        self.show_success("Download started! Check your downloads folder.")
    
    def show_success(self, message):
        self.ids.success_container.text = message
        self.ids.success_container.opacity = 1
        Clock.schedule_once(self.hide_success, 3)
    
    def hide_success(self, dt):
        self.ids.success_container.opacity = 0

class SavemediaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(DownloadScreen(name='download'))
        return sm

if __name__ == '__main__':
    SavemediaApp().run()
