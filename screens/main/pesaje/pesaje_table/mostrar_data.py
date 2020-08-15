# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.button import Button
# from kivy.uix.tabbedpanel import TabbedPanel
# from kivy.uix.gridlayout import GridLayout
# from kivy.properties import NumericProperty, ObjectProperty, StringProperty
# from kivymd.uix.picker import MDDatePicker

from kivy.lang import Builder

Builder.load_file('pesaje_table/mostrar_data.kv')


class MostrarData(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class mostrar_data(MDApp):
    def build(self):
        return MostrarData()


if __name__ == '__main__':
    mostrar_data().run()
