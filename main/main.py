from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from signin.signin import SigninWindow
from default.default import MainWid


class MainWindow(BoxLayout):

    signin_widget = SigninWindow()
    default_widget = MainWid()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_si.add_widget(self.signin_widget)
        self.ids.scrn_def.add_widget(self.default_widget)

class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
