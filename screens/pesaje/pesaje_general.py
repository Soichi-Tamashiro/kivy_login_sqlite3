# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel

from kivy.lang import Builder

# Builder.load_file('default/default.kv')

from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class PesajeGeneral(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class pesaje_general(App):
    def build(self):
        return PesajeGeneral()


if __name__ == '__main__':
    pesaje_general().run()
