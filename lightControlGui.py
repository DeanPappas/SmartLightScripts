from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
from phue import Bridge

b = Bridge('192.168.1.188')

kv_text = Builder.load_file("lightGUI.kv")
    

class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()

class FirstScreen(Screen):
    bright = 100
    def blue(self):
        b.set_light(1,'xy', (.01,.01))

    def red(self):
        b.set_light(1,'xy', (1,.5))

    def green(self):
        b.set_light(1,'xy', (.5,1))

    def yellow(self):
        b.set_light(1,'xy', (.5,.5))

    def addBri(self):
        bright = bright + 20
        b.set_light(1, 'bri', bright)

    def subBri(self):
        bright = bright - 20
        b.set_light(1, 'bri', bright)

class SecondScreen(Screen):
    bright = 100
    def teal(self):
        b.set_light(1,'xy', (.25,.45))

    def orange(self):
        b.set_light(1,'xy', (.6,.5))

    def violet(self):
        b.set_light(1,'xy', (.3,.1))

    def pink(self):
        b.set_light(1,'xy', (.45,.22))

    def addBri(self):
        bright = bright + 20
        b.set_light(1, 'bri', bright)

    def subBri(self):
        bright = bright - 20
        b.set_light(1, 'bri', bright)

class ThirdScreen(Screen):
    bright = 100
    def blue(self):
        b.set_light(1,'xy', (.01,.01))

    def red(self):
        b.set_light(1,'xy', (1,.5))

    def green(self):
        b.set_light(1,'xy', (.5,1))

    def yellow(self):
        b.set_light(1,'xy', (.5,.5))

    def addBri(self):
        bright = bright + 20
        b.set_light(1, 'bri', bright)

    def subBri(self):
        bright = bright - 20
        b.set_light(1, 'bri', bright)

class MyApp(App):
    def build(self):
        return MainScreen()

def main():
    b = Bridge('192.168.1.188')
    MyApp().run()

if __name__ == '__main__':
    main()