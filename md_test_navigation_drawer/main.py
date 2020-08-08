# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
    def build(self):
        # return Builder.load_string(KV)
        return Builder.load_file("main1.kv")


MainApp().run()
