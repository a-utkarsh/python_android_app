from kivy.app import App

from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
Builder.load_file('SimpleKivy.kv')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
class scan(Screen):
    def do_scan(self, target, range):
        app = App.get_running_app()

        app.target1 = target
        app.range1 = range

        self.manager.transition = SlideTransition(direction="left")
        app.config.read(app.get_application_config())
        app.config.write()



class SimpleKivy(App):
    def build(self):
        return scan()


if __name__ == "__main__":
    SimpleKivy().run()
