import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class CounterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0  # initialize the counter

    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Press me!', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)
        self.counter_label = Label(text='Counter: 0', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        layout.add_widget(self.counter_label)
        reset_button = Button(text='Reset', size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        reset_button.bind(on_press=self.reset_counter)
        layout.add_widget(reset_button)
        return layout

    def increment_counter(self, button):
        self.counter += 1
        self.counter_label.text = 'Counter: {}'.format(self.counter)

    def reset_counter(self, button):
        self.counter = 0
        self.counter_label.text = 'Counter: 0'


if __name__ == '__main__':
    CounterApp().run()