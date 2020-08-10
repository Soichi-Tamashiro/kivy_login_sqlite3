# -*- coding: utf-8 -*-
from kivy.config import Config
from kivy.lang import Builder
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
# from pesajetable1.pesajetable import PesajeTable


Builder.load_file('pesaje/pesajegeneral.kv')

# Config.set("graphics", "minimum_width", "800")
# Config.set("graphics", "minimum_height", "600")


class PesajeGeneral(BoxLayout):
    # pesaje_table_widget = PesajeTable()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.ids.tabla_pesaje.add_widget(self.pesaje_table_widget)

    # def on_enter(self, *args):


class pesajegeneral(App):
    def build(self):
        return PesajeGeneral()


if __name__ == '__main__':
    pesajegeneral().run()
