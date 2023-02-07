from kivy.config import Config

Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class abchixbaApp(App):
    def build(self):
        Window.size = (360, 800)
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Привет!')
        self.text_inp = TextInput(text='Цвет...')
        layout.add_widget(self.label)
        layout.add_widget(self.text_inp)
        colors = ['#ff0000', '#ff8800', '#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff']
        for i in range(7):
            btn = Button( background_color=colors[i], background_normal='', on_press=self.change)
            layout.add_widget(btn)
        return layout

    def change(self, instance):
        self.text_inp.text = instance.text
        colors = {'#ff0000': 'Красный',
                '#ff8800': 'Оранжевый',
                '#ffff00': 'Желтый',
                '#00ff00': 'Зеленый',
            '#00ffff': 'Голубой',
        '#0000ff': 'Синий',
        '#ff00ff': 'Фиолетовый'}
        self.label.text = colors.get(instance.text)

if __name__ == "__main__":
    abchixbaApp().run()