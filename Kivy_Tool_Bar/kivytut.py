import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
class SampGridlayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampGridlayout()



sample_app = SampleApp()
sample_app.run()
