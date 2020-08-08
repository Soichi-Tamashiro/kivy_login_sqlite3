from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
                self.parent.parent.current = 'scrn_def'

class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    sa = SigninApp()
    sa.run()
