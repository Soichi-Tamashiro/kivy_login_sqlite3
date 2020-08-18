# -*- coding: utf-8 -*-
from kivy.config import Config
import sqlite3
import os
import sys
from kivy.clock import Clock
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivymd.uix.picker import MDDatePicker
from kivy.uix.dropdown import DropDown
from kivymd.uix.menu import MDDropdownMenu

from search.search_empresa import SearchEmpresa

from kivy.lang import Builder

Builder.load_file('pesaje_table/ingresar_data.kv')

Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class IngresarData(BoxLayout):
    empresa_field_widget = SearchEmpresa()
    # ticket_field = ObjectProperty()
    empresa_field = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/data/my_database.db"
        print("Dirección: ", self.DB_PATH)
        self.ids.empresa_field.add_widget(self.empresa_field_widget)
        # self.empresa_field_widget.get_focus_next()
        #get_focus_next() self.empresa_field_widget.bind(on_text_validate=self.empresa_field.focus=True)

    def update_ticket(self, *args):
        return self.ids.ticket_field.text

    def update_empresa(self, *args):
        return str(self.empresa_field_widget.text)

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

    def clear_data(self, dataton):
        self.ids.ticket_field.text = ""
        self.empresa_field_widget.text = ""
        self.ids.bascula_field.text = ""
        self.ids.placa_field.text = ""
        self.ids.ciclo_pesaje_field.text = ""
        self.ids.fecha_entrada_field.text = "dd/mm/yyyy"
        self.ids.peso_entrada_field.text = ""
        self.ids.fecha_salida_field.text = "dd/mm/yyyy"
        self.ids.peso_salida_field.text = ""
        self.ids.peso_neto_field.text = ""
        self.empresa_field_widget.update_empresa_db()
        # self.ids.empresa_field.clear_widgets()
        # self.ids.empresa_field.add_widget(self.empresa_field_widget)
        print(dataton)

    # def search_empresa(self):
    #     print(self.ids.empresa_field.text)
    #     con = sqlite3.connect(self.DB_PATH)
    #     cursor = con.cursor()
    #     cursor.execute(
    #         'select ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto from Data')
    #     data_file = cursor.fetchall()
    #     empresa_array = [""] * len(data_file[2])
    #     for i in range(len(data_file)):
    #         empresa_array[i] = data_file[i][2]
    #         print(empresa_array[i])

        # self.word_list = data_file[0]

    # def on_text(self, instance, value):
    #     # include all current text from textinput into the word list
    #     # the kind of behavior sublime text has
    #     self.suggestion_text = ''
    #     word_list = list(set(self.word_list + value[:value.rfind(' ')].split(' ')))
    #     val = value[value.rfind(' ')+1:]
    #     if not val: return
    #     try:
    #         # grossly ineffecient just for demo purposes
    #         word = [word for word in word_list if word.startswith(val)][0][len(val):]
    #         if not word: return
    #         self.root.suggestion_text = word
    #     except IndexError:
    #         print ('Index Error')
    #     self.dropdown.items.append(
    #         {"viewclass": "MDMenuItem",
    #          "text": "Option 1",
    #          "callback": self.option_callback
    #          }
    #     # self.dropdown = MDDropdownMenu()
    #     # for i in range(len(array_data)):
    #     #     self.dropdown.items.append(
    #     #         {"viewclass": "MDMenuItem",
    #     #          "text": "Option 1",
    #     #          "callback": self.option_callback
    #     #          }
    #     #     )
    #         # HB = BoxLayout(orientation='horizontal')
    #         # self.ids.container2.add_widget(HB)
    #         # for j in range(1, len(array_data[i])):
    #         #     l1 = Label(text=str(array_data[i][j]))
    #         #     HB.add_widget(l1)
    #     pass
    # def option_callback(self, text_of_the_option):
    #     print(text_of_the_option)


class ingresar_data(MDApp):
    # ingresar_data_dict = {}

    def build(self):
        return IngresarData()


if __name__ == '__main__':
    ingresar_data().run()
