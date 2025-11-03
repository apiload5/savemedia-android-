from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SavemediaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Savemedia', font_size=24))
        layout.add_widget(TextInput(hint_text='Paste URL', size_hint_y=None, height=50))
        layout.add_widget(Button(text='DOWNLOAD', size_hint_y=None, height=60))
        return layout

if __name__ == '__main__':
    SavemediaApp().run()
