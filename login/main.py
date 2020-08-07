# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid, self).__init__()
        self.StartWid = StartWid()

        wid = Screen(name="start")
        wid.add_widget(self.StartWid)
        self.add_widget(wid)


class StartWid(BoxLayout):
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

    pass


class MainApp(App):
    title = 'Test Pesaje'

    def build(self):
        return MainWid()


if __name__ == '__main__':
    MainApp().run()
