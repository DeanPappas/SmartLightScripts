#https://kivy.org/#home to install kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
from phue import Bridge

b = Bridge('192.168.1.188')

class MyGrid(GridLayout):
    bright = 254
    def __init__(self, **kwargs):
        # ----------------------------------- Create elements -----------------------------------
        super(MyGrid, self).__init__(**kwargs)
        # Main Container
        self.cols = 1
        # Sub containers
        self.topRow = GridLayout()
        self.topRow.cols = 3
        self.bottomRow = GridLayout()
        self.bottomRow.cols = 3
        
        # Brightness + button
        self.addBrightButton = Button(text ="+", font_size = 50)
        self.addBrightButton.background_color = (.5, .5, .5, 1)
        self.addBrightButton.bind(on_press=self.addBrightPressed)
        # Brightness - button
        self.subBrightButton = Button(text ="-", font_size = 50)
        self.subBrightButton.background_color = (.5, .5, .5, 1)
        self.subBrightButton.bind(on_press=self.subBrightPressed)
        # Blue button
        self.blueButton = Button(text ="", font_size = 30)
        self.blueButton.background_color = (0, 0, 1, 1)
        self.blueButton.bind(on_press=self.blueButtonPressed)
        # Red button
        self.redButton = Button(text ="", font_size = 30)
        self.redButton.background_color = (1, 0, 0, 1)
        self.redButton.bind(on_press=self.redButtonPressed)
        # Green button
        self.greenButton = Button(text ="", font_size = 30)
        self.greenButton.background_color = (0, 1, 0, 1)
        self.greenButton.bind(on_press=self.greenButtonPressed)
        # Yellow button
        self.yellowButton = Button(text ="", font_size = 30)
        self.yellowButton.background_color = (1, 1, 0, 1)
        self.yellowButton.bind(on_press=self.yellowButtonPressed)
        
        
        # ----------------------------------- Add elements -----------------------------------
        self.add_widget(self.topRow) # Add top row container
        self.add_widget(self.bottomRow) # Add bottom row container
        self.topRow.add_widget(self.blueButton) # Add blueButton
        self.topRow.add_widget(self.redButton) # Add redButton
        self.topRow.add_widget(self.addBrightButton) # Add brightness + button
        self.bottomRow.add_widget(self.greenButton) # Add greenButton
        self.bottomRow.add_widget(self.yellowButton) # Add yellowButton
        self.bottomRow.add_widget(self.subBrightButton) # Add brightness - button
        
        
        
    # ----------------------------------- Button Press Actions -----------------------------------  
    def addBrightPressed(self, instance):
        b.set_light(1, 'bri', 254)
        print("add bright")
        pass
    
    def subBrightPressed(self, instance):
        b.set_light(1, 'bri', 100)
        print("sub bright")
        pass
    
    def blueButtonPressed(self, instance):
        print("blue")
        b.set_light(1,'xy', (.01,.01))
        pass
    
    def redButtonPressed(self, instance):
        print("red")
        b.set_light(1,'xy', (1,.5))
        pass
    
    def greenButtonPressed(self, instance):
        print("greeb")
        b.set_light(1,'xy', (.5,1))
        pass
    
    def yellowButtonPressed(self, instance):
        print("yellow")
        b.set_light(1,'xy', (.5,.5))
        pass
        
# ----------------------------------- Running the app -----------------------------------
class MyApp(App):
    def build(self):
        return MyGrid()
    
        
if __name__ == "__main__":
    MyApp().run()