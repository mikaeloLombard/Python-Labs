import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class K_kivy2App(App):

    def build(self):
        return FloatLayout()

flApp = K_kivy2App()
flApp.run()