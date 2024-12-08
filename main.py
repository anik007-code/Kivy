from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        screen = Screen()
        label = Label(text="Hello, Kivy!", font_size=32)
        screen.add_widget(label)
        return screen

if __name__ == '__main__':
    MyApp().run()
