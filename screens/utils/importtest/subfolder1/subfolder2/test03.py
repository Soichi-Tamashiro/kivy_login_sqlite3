import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

# Builder.load_file('subfolder2/test_03.kv')

from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class Test03(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class test_03(App):
    def build(self):
        return Test03()


if __name__ == '__main__':
    test_03().run()
