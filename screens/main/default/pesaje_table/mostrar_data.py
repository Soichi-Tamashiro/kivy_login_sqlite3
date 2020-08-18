# -*- coding: utf-8 -*-
from kivy.config import Config
import sqlite3
import os

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.button import Button
# from kivy.uix.tabbedpanel import TabbedPanel
# from kivy.uix.gridlayout import GridLayout
# from kivy.properties import NumericProperty, ObjectProperty, StringProperty
# from kivymd.uix.picker import MDDatePicker

from kivy.lang import Builder

Builder.load_file('pesaje_table/mostrar_data.kv')


Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class MostrarData(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def crear_fila1(self, array_data):
        self.ids.container2.clear_widgets()
        # print("Cantidad de columnas : " + str(len(array_data[0])))
        # print("Cantidad de filas : " + str(len(array_data)))
        for i in range(len(array_data)):
            HB = BoxLayout(orientation='horizontal')
            self.ids.container2.add_widget(HB)
            for j in range(1, len(array_data[i])):
                l1 = Label(text=str(array_data[i][j]))
                HB.add_widget(l1)
                # print(array_data[i][j])

    def crear_fila(self, r1, r3, r4, r5, r6, r7, r8, r9, r10, r11):
        #     print(r1)
        HB = BoxLayout(orientation='horizontal')
        l1 = Label(text=r1)
        # l2 = Label(text=r2)
        l3 = Label(text=r3)
        l4 = Label(text=r4)
        l5 = Label(text=r5)
        l6 = Label(text=r6)
        l7 = Label(text=r7)
        l8 = Label(text=r8)
        l9 = Label(text=r9)
        l10 = Label(text=r10)
        l11 = Label(text=r11)
        self.ids.container2.add_widget(HB)
        HB.add_widget(l1)
        # HB.add_widget(l2)
        HB.add_widget(l3)
        HB.add_widget(l4)
        HB.add_widget(l5)
        HB.add_widget(l6)
        HB.add_widget(l7)
        HB.add_widget(l8)
        HB.add_widget(l9)
        HB.add_widget(l10)
        HB.add_widget(l11)
        pass


class mostrar_data(MDApp):
    def build(self):
        return MostrarData()


if __name__ == '__main__':
    mostrar_data().run()
