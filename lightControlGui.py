from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import requests

Config.set('graphics', 'fullscreen', 'auto')
from phue import Bridge

# Get Hue Hub IP address from Phillips Hue API
response = requests.get("https://discovery.meethue.com/")
response.raise_for_status()
data = response.json()
hub_ip = data[0]["internalipaddress"]

# Set IP from Philips Hue Bridge
b = Bridge(hub_ip)
# Set light names from Hue App
light1 = "Desk Light"
light2 = "Corner Light"
b.connect()

kv_text = Builder.load_file("lightGUI.kv")


class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()


class FirstScreen(Screen):

    def powerOn(self):
        b.set_light(light1, 'on', True)
        b.set_light(light2, 'on', True)

    def powerOff(self):
        b.set_light(light1, 'on', False)
        b.set_light(light2, 'on', False)


class SecondScreen(Screen):
    bri = b.get_light(light1, 'bri')
    bri = b.get_light(light2, 'bri')

    def blue(self):
        b.set_light(light1, 'xy', (.01, .01))
        b.set_light(light2, 'xy', (.01, .01))

    def red(self):
        b.set_light(light1, 'xy', (1, .5))
        b.set_light(light2, 'xy', (1, .5))

    def green(self):
        b.set_light(light1, 'xy', (.5, 1))
        b.set_light(light2, 'xy', (.5, 1))

    def yellow(self):
        b.set_light(light1, 'xy', (.5, .5))
        b.set_light(light2, 'xy', (.5, .5))

    def addBri(self):
        if self.bri > 240:
            print(self.bri)
            self.bri = 254
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)

    def subBri(self):
        if self.bri < 20:
            print(self.bri)
            self.bri = 1
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)


class ThirdScreen(Screen):
    bri = b.get_light(light1, 'bri')
    bri = b.get_light(light2, 'bri')

    def teal(self):
        b.set_light(light1, 'xy', (.25, .45))
        b.set_light(light2, 'xy', (.25, .45))

    def orange(self):
        b.set_light(light1, 'xy', (0.614, 0.3783))
        b.set_light(light2, 'xy', (0.614, 0.3783))

    def violet(self):
        b.set_light(light1, 'xy', (.3, .1))
        b.set_light(light2, 'xy', (.3, .1))

    def pink(self):
        b.set_light(light1, 'xy', (0.3971, 0.225))
        b.set_light(light2, 'xy', (0.3971, 0.225))

    def addBri(self):
        if (self.bri > 240):
            print(self.bri)
            self.bri = 254
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)

    def subBri(self):
        if self.bri < 20:
            print(self.bri)
            self.bri = 1
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)


class FourthScreen(Screen):
    bri = b.get_light(light1, 'bri')
    bri = b.get_light(light2, 'bri')

    def blue(self):
        b.set_light(light1, 'xy', (.01, .01))
        b.set_light(light2, 'xy', (.01, .01))

    def red(self):
        b.set_light(light1, 'xy', (1, .5))
        b.set_light(light2, 'xy', (1, .5))

    def green(self):
        b.set_light(light1, 'xy', (.5, 1))
        b.set_light(light2, 'xy', (.5, 1))

    def yellow(self):
        b.set_light(light1, 'xy', (.5, .5))
        b.set_light(light2, 'xy', (.5, .5))

    def addBri(self):
        if self.bri > 240:
            print(self.bri)
            self.bri = 254
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri + 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)

    def subBri(self):
        if self.bri < 20:
            print(self.bri)
            self.bri = 1
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)
        else:
            print(self.bri)
            self.bri = self.bri - 20
            b.set_light(light1, 'bri', self.bri)
            b.set_light(light2, 'bri', self.bri)


class MyApp(App):
    def build(self):
        return MainScreen()


def main():
    MyApp().run()


if __name__ == '__main__':
    main()
