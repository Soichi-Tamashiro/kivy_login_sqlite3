# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel

# from utils.table import TableWid
from pesaje.pesajegeneral import PesajeGeneral
# from pesajetable1.pesajetable import PesajeTable
from kivy.lang import Builder

Builder.load_file('default/default.kv')

from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class MainWid(BoxLayout):
    ## table_widget = TableWid()
    pesaje_gen_widget = PesajeGeneral()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ## self.ids.container2.add_widget(self.table_widget)
        self.ids.scrn_pesaje_gen.add_widget(self.pesaje_gen_widget)


    def change_screen(self, instance):
        if instance.text == '- Bascula':
            self.ids.scrn_mngr.current = 'scrn_bascula'
        elif instance.text == '- Pesaje General':
            self.ids.scrn_mngr.current = 'scrn_pesaje_gen'
        elif instance.text == '- Empresa':
            self.ids.scrn_mngr.current = 'scrn_empresa'
        else:
            pass

    # def change_screen_pesaje(self, instance):
    #     if instance.text == 'Gestion Pesaje Vehiculo':
    #         self.ids.scrn_mngr.current = 'scrn_pesaje'
    #
    #     elif instance.text == 'Gestion Consulta Vehiculo':
    #         self.ids.scrn_mngr.current = 'scrn_consulta'
    #     else:
    #         pass


class Default(App):
    def build(self):
        return MainWid()


if __name__ == '__main__':
    Default().run()
