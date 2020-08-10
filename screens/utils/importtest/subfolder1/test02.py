import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from .subfolder2.test03 import  Test03

from kivy.lang import Builder

# Builder.load_file('pesaje_table/pesaje_table.kv')

from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class Test02(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class test_02(App):
    def build(self):
        return Test02()


if __name__ == '__main__':
    test_02().run()
