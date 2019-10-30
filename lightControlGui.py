from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import ObjectProperty
Config.set('graphics', 'fullscreen', 'auto')
from phue import Bridge

b = Bridge('192.168.1.188')

kv_text = Builder.load_file("lightGUI.kv")
    

class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()

class FirstScreen(Screen):
    
    def powerOn(self):
        b.set_light(1,'on', True)
    
    def powerOff(self):
        b.set_light(1,'on', False)

class SecondScreen(Screen):

    bri = b.get_light(1,'bri')
    
    def blue(self):
        b.set_light(1,'xy', (.01,.01))

    def red(self):
        b.set_light(1,'xy', (1,.5))

    def green(self):
        b.set_light(1,'xy', (.5,1))

    def yellow(self):
        b.set_light(1,'xy', (.5,.5))

    def addBri(self):
        if(self.bri > 240):
            print(self.bri)
            self.bri = 254
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(1, 'bri', self.bri)

    def subBri(self):
        if(self.bri < 20):
            print(self.bri)
            self.bri = 1
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(1, 'bri', self.bri)

class ThirdScreen(Screen):

    bri = b.get_light(1,'bri')
    
    def teal(self):
        b.set_light(1,'xy', (.25,.45))

    def orange(self):
        b.set_light(1,'xy', (.6,.5))

    def violet(self):
        b.set_light(1,'xy', (.3,.1))

    def pink(self):
        b.set_light(1,'xy', (.45,.22))

    def addBri(self):
        if(self.bri > 240):
            print(self.bri)
            self.bri = 254
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(1, 'bri', self.bri)

    def subBri(self):
        if(self.bri < 20):
            print(self.bri)
            self.bri = 1
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(1, 'bri', self.bri)

class FourthScreen(Screen):
    
    bri = b.get_light(1,'bri')
   
    def blue(self):
        b.set_light(1,'xy', (.01,.01))

    def red(self):
        b.set_light(1,'xy', (1,.5))

    def green(self):
        b.set_light(1,'xy', (.5,1))

    def yellow(self):
        b.set_light(1,'xy', (.5,.5))

    def addBri(self):
        if(self.bri > 240):
            print(self.bri)
            self.bri = 254
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(1, 'bri', self.bri)

    def subBri(self):
        if(self.bri < 20):
            print(self.bri)
            self.bri = 1
            b.set_light(1,'bri',self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(1, 'bri', self.bri)

class MyApp(App):
    def build(self):
        return MainScreen()

def main():
    b = Bridge('192.168.1.188')
    MyApp().run()

if __name__ == '__main__':
    main()