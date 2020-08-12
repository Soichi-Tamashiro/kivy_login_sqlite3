# -*- coding: utf-8 -*-
from kivy.config import Config
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from pesaje_table.pesaje_table import PesajeTable

from kivy.lang import Builder

Builder.load_file('pesaje/pesaje_general.kv')


Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


def connect_to_database(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_users(cursor)
        create_table_data(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_data(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)


def create_table_users(cursor):
    cursor.execute(
        '''
        CREATE TABLE Users(
        ID        INT   PRIMARY KEY  NOT NULL,
        Nombre    TEXT               NOT NULL,
        Password  TEXT               NOT NULL,
        Cargo     TEXT               NOT NULL
        )
        '''
    )


def create_table_data(cursor):
    cursor.execute(
        '''
        CREATE TABLE Data(
        ID              INT   PRIMARY KEY  NOT NULL,
        Ticket          TEXT               NOT NULL,
        Empresa         TEXT               NOT NULL,
        Bascula         TEXT               NOT NULL,
        Placa           TEXT               NOT NULL,
        CicloPesaje     TEXT               NOT NULL ,
        FechaEntrada    TEXT               NOT NULL ,
        PesoEntrada     TEXT               NOT NULL ,
        FechaSalida     TEXT               NOT NULL ,
        PesoSalida      TEXT               NOT NULL ,
        PesoNeto        TEXT               NOT NULL
        )
        '''
    )


class PesajeGeneral(BoxLayout):
    pesaje_table_widget = PesajeTable()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/data/my_database.db"
        print("Dirección: ", self.DB_PATH)
        connect_to_database(self.DB_PATH)
        # Add widget ti views
        # self.ids.tabla_pesaje.add_widget(self.pesaje_table_widget)

    def ingresar_pesaje(self):
        print("NUEVO PESAJE")
        pass

    # def on_enter(self):
    #     print("Creating DB")


class pesaje_general(App):
    def build(self):
        return PesajeGeneral()


if __name__ == '__main__':
    pesaje_general().run()
