# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivymd.uix.picker import MDDatePicker

from kivy.lang import Builder

Builder.load_file('pesaje_table/ingresar_data.kv')

# from kivy.config import Config
# Config.set("graphics", "minimum_width", "800")
# Config.set("graphics", "minimum_height", "600")


class IngresarData(BoxLayout):
    # ticket_field = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_ticket(self, *args):
        return self.ids.ticket_field.text

    def update_empresa(self, *args):
        return self.ids.empresa_field.text

    def update_bascula(self, *args):
        return self.ids.bascula_field.text

    def update_placa(self, *args):
        return self.ids.placa_field.text

    def update_ciclo_pesaje(self, *args):
        return self.ids.ciclo_pesaje_field.text

    def show_datepicker_1(self):
        picker = MDDatePicker(callback=self.got_date_1)
        picker.open()

    def got_date_1(self, the_date):
        print(the_date.year)
        print(the_date.month)
        print(the_date.day)
        print(the_date)
        self.ids.fecha_entrada_field.text = str(
            the_date.day) + '/' + str(the_date.month) + '/' + str(the_date.year)
        return self.ids.fecha_entrada_field.text

    def update_fecha_entrada(self, *args):
        return self.ids.fecha_entrada_field.text

    def update_peso_entrada(self, *args):
        return self.ids.peso_entrada_field.text

    def show_datepicker_2(self):
        picker = MDDatePicker(callback=self.got_date_2)
        picker.open()

    def got_date_2(self, the_date):
        self.ids.fecha_salida_field.text = str(
            the_date.day) + '/' + str(the_date.month) + '/' + str(the_date.year)
        return self.ids.fecha_salida_field.text

    def update_fecha_salida(self, *args):
        return self.ids.fecha_salida_field.text

    def update_peso_salida(self, *args):
        return self.ids.peso_salida_field.text

    def update_peso_neto(self, *args):
        return self.ids.peso_neto_field.text

    def clear_data(self):
        self.ids.ticket_field.text = ""


class ingresar_data(MDApp):
    # ingresar_data_dict = {}

    def build(self):
        return IngresarData()


if __name__ == '__main__':
    ingresar_data().run()
