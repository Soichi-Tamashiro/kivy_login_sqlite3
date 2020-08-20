from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
import kivy
kivy.require('1.9.0')


class MainScreen(FloatLayout):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.has_sidebar = False

    def menu_action(self):
        if not self.has_sidebar:
            print('adding sidebar')
            self.add_widget(SideBar())
            self.has_sidebar = True
        else:
            print('not adding sidebar')


class SideBar(FloatLayout):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('inside side')
        else:
            print('outside side')


class side_bar(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    side_bar().run()
