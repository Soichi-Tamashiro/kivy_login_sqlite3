# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from kivy.lang import Builder

# Builder.load_file('default/default.kv')

from kivy.config import Config
Config.set("graphics", "width", "800")
Config.set("graphics", "heighth", "600")


class MainWid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Default(App):
    def build(self):
        return MainWid()


if __name__ == '__main__':
    Default().run()
