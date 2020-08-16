# -*- coding: utf-8 -*-
from kivy.config import Config
import sqlite3
import os

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
# from pesaje_table.pesaje_table import PesajeTable
from pesaje_table.ingresar_data import IngresarData
from pesaje_table.mostrar_data import MostrarData

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
    # pesaje_table_widget = PesajeTable()
    ingresar_data_widget = IngresarData()
    mostrar_data_widget = MostrarData()
    # nuevo_pesaje_button = ObjectProperty()
    # guardar_pesaje_button = ObjectProperty()
    number = NumericProperty(0)
    mostrar_data_state = NumericProperty(0)

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
        # print(self.number)
        if(self.number == 1):
            self.number = 0
            print(self.number)
            # self.ids.tabla_pesaje.remove_widget(self.pesaje_table_widget)
            self.ids.tabla_pesaje.remove_widget(self.ingresar_data_widget)
            self.ids.nuevo_pesaje_button.text = 'Nuevo Pesaje'
            self.ids.guardar_pesaje_button.disabled = True
            self.ids.mostrar_data_button.disabled = False
        elif(self.number == 0):
            self.number = 1
            print(self.number)
            self.ids.tabla_pesaje.add_widget(self.ingresar_data_widget)
            self.ids.nuevo_pesaje_button.text = 'Cerrar'
            self.ids.guardar_pesaje_button.disabled = False
            self.ids.mostrar_data_button.disabled = True
            # for child in self.ids.tabla_pesaje.children:
            #     print(child)
        pass
        # self.ids.tabla_pesaje.add_widget(self.pesaje_table_widget)

    def guardar_pesaje(self):
        # c = App.get_running_app()
        print("GUARDAR PESAJE")
        if(self.number == 1):
            self.number = 0
            print(self.number)
            # update table
            Ticket = self.ingresar_data_widget.update_ticket()
            ID = Ticket
            Empresa = self.ingresar_data_widget.update_empresa()
            Bascula = self.ingresar_data_widget.update_bascula()
            Placa = self.ingresar_data_widget.update_placa()
            CicloPesaje = self.ingresar_data_widget.update_ciclo_pesaje()
            FechaEntrada = self.ingresar_data_widget.update_fecha_entrada()
            PesoEntrada = self.ingresar_data_widget.update_peso_entrada()
            FechaSalida = self.ingresar_data_widget.update_fecha_salida()
            PesoSalida = self.ingresar_data_widget.update_peso_salida()
            PesoNeto = self.ingresar_data_widget.update_peso_neto()
            # Test if one value is empty for conneting to db
            if(Ticket != "" and Empresa != "" and Bascula != "" and Placa != "" and CicloPesaje != "" and FechaEntrada != "" and PesoEntrada != "" and FechaSalida != "" and PesoSalida != "" and PesoNeto):
                con = sqlite3.connect(self.DB_PATH)
                print(self.DB_PATH)
                cursor = con.cursor()
                datos = (ID, Ticket, Empresa, Bascula, Placa, CicloPesaje,
                         FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto)
                #
                s1 = 'INSERT INTO Data(ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto)'
                #
                s2 = 'VALUES(%s,"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % datos
                try:
                    cursor.execute(s1 + ' ' + s2)
                    con.commit()
                    con.close()
                except Exception as e:
                    print(e)
                # update buttons
                self.nuevo_pesaje_button.text = 'Nuevo Pesaje'
                self.guardar_pesaje_button.disabled = True
                # remove_widget
                self.ids.tabla_pesaje.remove_widget(
                    self.ingresar_data_widget)
                # clear_data
                dataton = "limpiado"
                self.ingresar_data_widget.clear_data(dataton)
                print("PESAJE GUARDADO CON EXITO")
            else:
                self.number = 1
                print(self.number)
            pass
            # con = sqlite3.connect(self.DB_PATH)
            # cursor = con.cursor()
            # d1 = self.ingresar_data_widget.ingresar_data.ticket_field.text
            # d1 = self.ids.tabla_pesaje.ingresar_data.ticket_field.text

        # elif(self.number == 0):
        #     self.number = 1
        #     print(self.number)
        #     self.ids.tabla_pesaje.add_widget(self.ingresar_data_widget)
        #     self.nuevo_pesaje_button.text = 'Cerrar'
        #     self.guardar_pesaje_button.disabled = False

    def muestra_data(self):
        print("MUESTRA DATA")
        if(self.mostrar_data_state == 1):
            self.mostrar_data_state = 0
            print(self.mostrar_data_state)
            self.ids.tabla_pesaje.remove_widget(self.mostrar_data_widget)
            self.ids.mostrar_data_button.text = 'Consulta'
            self.ids.guardar_pesaje_button.disabled = False
            self.ids.nuevo_pesaje_button.disabled = False
            self.ids.cantidad_registros.text = ""
        elif(self.mostrar_data_state == 0):
            self.mostrar_data_state = 1
            print(self.mostrar_data_state)
            self.ids.tabla_pesaje.add_widget(self.mostrar_data_widget)
            self.ids.mostrar_data_button.text = 'Cerrar'
            self.ids.guardar_pesaje_button.disabled = True
            self.ids.nuevo_pesaje_button.disabled = True
            con = sqlite3.connect(self.DB_PATH)
            cursor = con.cursor()
            cursor.execute(
                'select ID, Ticket,Empresa, Bascula, Placa, CicloPesaje, FechaEntrada, PesoEntrada, FechaSalida, PesoSalida, PesoNeto from Data')
            data_file = cursor.fetchall()
            numero_de_registros = str(len(data_file))
            print("Cantidad de registros : "+numero_de_registros)
            self.mostrar_data_widget.crear_fila1(data_file)
            self.ids.cantidad_registros.text = "Cantidad de Registros: " + numero_de_registros
            # print(self.ids.cantidad_registros.text)
            # print(len(data_file))
            # for i in range(len(data_file)):
            # data_file[fila][columna]
            # print(data_file[3][2])
            # for i in cursor:
            #     r1 = str(100000 + i[0])[1:6]  # + '\n'
            #     # r2 = str(10000 + i[1])[1:5]
            #     r3 = str(i[2])
            #     r5 = str(i[4])
            #     r4 = str(i[3])
            #     r6 = str(i[5])
            #     r9 = str(i[8])
            #     r7 = str(i[6])
            #     r8 = str(i[7])
            #     r10 = str(i[9])
            #     r11 = str(i[10])
            #     # print(r1)
            #     self.mostrar_data_widget.crear_fila(
            #         r1, r3, r4, r5, r6, r7, r8, r9, r10, r11)
            #     # self.mostrar_data_widget.crear_fila(r1)
            #     # self.mostrar_data_widget.crear_fila(r3)
            #     for row in range(0, 10):
            #         # print(i[row])

            con.close()
        pass


class pesaje_general(MDApp):
    # ingresar_data_dict_2 = {}

    def build(self):
        return PesajeGeneral()


if __name__ == '__main__':
    pesaje_general().run()
