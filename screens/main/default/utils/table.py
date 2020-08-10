from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('utils/table.kv')


class TableWid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Table(App):
    def build(self):
        return TableWid()


if __name__ == '__main__':
    Table().run()
