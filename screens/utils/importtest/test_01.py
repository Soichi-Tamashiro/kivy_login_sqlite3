# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from subfolder1.test02 import  Test02

from kivy.lang import Builder

# Builder.load_file('pesaje_table/pesaje_table.kv')

from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class Test01(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class test_01(App):
    def build(self):
        return Test01()


if __name__ == '__main__':
    test_01().run()
