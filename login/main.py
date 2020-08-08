# -*- coding: utf-8 -*-
import sqlite3
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from kivy.config import Config
Config.set("graphics", "width", "800")
Config.set("graphics", "heighth", "600")


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
        ID        INT   PRIMARY KEY  NOT NULL,
        Empresa   TEXT               NOT NULL,
        Bascula   TEXT               NOT NULL,
        Placa     TEXT               NOT NULL
        )
        '''
    )


class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid, self).__init__()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/data/my_database.db"
        self.StartWid = StartWid(self)
        self.DefaultWid = DefaultWid(self)

        wid = Screen(name='start')
        wid.add_widget(self.StartWid)
        self.add_widget(wid)
        wid = Screen(name='default')
        wid.add_widget(self.DefaultWid)
        self.add_widget(wid)

        self.goto_start()

    def goto_start(self):
        self.current = 'start'

    def goto_default(self):
        self.current = 'default'

class StartWid(BoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(StartWid, self).__init__()
        self.mainwid = mainwid

    def create_database(self):
        connect_to_database(self.mainwid.DB_PATH)
        self.mainwid.goto_default()

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if (uname == '' or passw == ''):
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            if (uname == 'admin' and passw == 'admin'):
                info.text = '[color=#00FF00]Logged In succesfully !!![/color]'

class DefaultWid(BoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(DefaultWid, self).__init__()
        self.mainwid = mainwid


class MainApp(App):
    title = 'Test Pesaje'

    def build(self):
        return MainWid()


if __name__ == '__main__':
    MainApp().run()
