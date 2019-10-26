from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
from phue import Bridge

kv_text = Builder.load_file("lightGUI.kv")
    

class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()

class FirstScreen(Screen):
    #some methods
    pass

class SecondScreen(Screen):
    #some methods
    pass
    
class ThirdScreen(Screen):
    #some methods
    pass

class MyApp(App):
    def build(self):
        return MainScreen()

def main():
    MyApp().run()

if __name__ == '__main__':
    main()