# -*- coding: utf-8 -*-
'''This is a simple example of how to use suggestion text.
In this example you setup a word_list at the begining. In this case
'the the quick brown fox jumps over the lazy old dog'. This list along
with any new word written word in the textinput is available as a
suggestion when you are typing. You can press tab to auto complete the text.
'''
import sys
import sqlite3
import os
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

# Builder.load_file('pesaje_table/search_empresa.kv')
# Builder.load_string('''
# <SearchEmpresa>:
#     readonly:False
#     multiline:False
#     focus: True
# ''')
from kivy.config import Config
Config.set("graphics", "minimum_width", "800")
Config.set("graphics", "minimum_height", "600")


class SearchEmpresa(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.write_tab = False
        self.text = ""
        self.bind(text=self.on_text)
        # self.word_list = ('the the quick brown fox jumps over the lazy old dog').split(' ')
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH + "/data/my_database.db"
        print("Dirección: ", self.DB_PATH)
        con = sqlite3.connect(self.DB_PATH)
        cursor = con.cursor()
        cursor.execute(
            'select ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto from Data')
        data_file = cursor.fetchall()
        empresa_array = [""] * len(data_file[2])
        for i in range(len(data_file)):
            # empresa_array[i] = str(data_file[i][2])
            empresa_array.insert(i, str(data_file[i][2]))
            print(empresa_array[i])
        self.word_list = empresa_array

    def update_empresa_db(self, **kwargs):
        con = sqlite3.connect(self.DB_PATH)
        cursor = con.cursor()
        cursor.execute(
            'select ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto from Data')
        data_file = cursor.fetchall()
        empresa_array = [""] * len(data_file[2])
        for i in range(len(data_file)):
            # empresa_array[i] = str(data_file[i][2])
            empresa_array.insert(i, str(data_file[i][2]))
            print(empresa_array[i])
        self.word_list = empresa_array

    def on_text_validate(self):
        print('User pressed enter')

    def on_text(self, instance, value):
        # include all current text from textinput into the word list
        # the kind of behavior sublime text has
        self.suggestion_text = ''
        word_list = list(
            set(self.word_list + value[:value.rfind(' ')].split(' ')))
        val = value[value.rfind(' ') + 1:]
        if not val:
            return
        try:
            # grossly ineffecient just for demo purposes
            word = [word for word in word_list if word.startswith(
                val)][0][len(val):]
            if not word:
                return
            self.suggestion_text = word
        except IndexError:
            print ('Index Error')

    def on_suggestion_text(self, instance, value):
        if not value:
            return
        super(SearchEmpresa, self).on_suggestion_text(instance, value)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        '''
        '''
        if self.suggestion_text and (keycode[1] == 'enter' or keycode[1] == 'tab'):  # complete suggestion_text
            self.insert_text(self.suggestion_text + ' ')
            self.suggestion_text = ''
            return True
        return super(SearchEmpresa, self).keyboard_on_key_down(window, keycode, text, modifiers)


class search_empresa(MDApp):

    # def on_start(self):
    #     self.root.text = ""
    #     self.root.bind(text=self.on_text)
    #     # self.word_list = ('the the quick brown fox jumps over the lazy old dog').split(' ')
    #     self.APP_PATH = os.getcwd()
    #     self.DB_PATH = self.APP_PATH + "/data/my_database.db"
    #     print("Dirección: ", self.DB_PATH)
    #     con = sqlite3.connect(self.DB_PATH)
    #     cursor = con.cursor()
    #     cursor.execute(
    #         'select ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto from Data')
    #     data_file = cursor.fetchall()
    #     empresa_array = [""] * len(data_file[2])
    #     for i in range(len(data_file)):
    #         empresa_array[i] = data_file[i][2]
    #         print(empresa_array[i])
    #     self.word_list = empresa_array
    #
    # def on_text(self, instance, value):
    #     # include all current text from textinput into the word list
    #     # the kind of behavior sublime text has
    #     self.suggestion_text = ''
    #     word_list = list(
    #         set(self.word_list + value[:value.rfind(' ')].split(' ')))
    #     val = value[value.rfind(' ') + 1:]
    #     if not val:
    #         return
    #     try:
    #         # grossly ineffecient just for demo purposes
    #         word = [word for word in word_list if word.startswith(
    #             val)][0][len(val):]
    #         if not word:
    #             return
    #         self.root.suggestion_text = word
    #     except IndexError:
    #         print ('Index Error')

    def build(self):
        # return SearchEmpresa()
        return Builder.load_file('search/search_empresa.kv')
#         return Builder.load_string('''
# SearchEmpresa
#     readonly:False
#     multiline:False
#     focus: True
# ''')


if __name__ == "__main__":
    search_empresa().run()
