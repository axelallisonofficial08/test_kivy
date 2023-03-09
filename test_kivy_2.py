import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        
        # Set the orientation of the BoxLayout to vertical
        self.orientation = 'vertical'
        
        # Create a horizontal BoxLayout for each row of buttons
        row_layout1 = BoxLayout(size_hint=(None, None), height=200)
        row_layout1.spacing = 10
        row_layout1.padding = [10, 10, 0, 100]

        button1 = Button(text='Test Page 1', size_hint=(None, 1), width=300)
        button2 = Button(text='Test Page 2', size_hint=(None, 1), width=300)

        row_layout1.add_widget(button1)
        row_layout1.add_widget(button2)

        self.add_widget(row_layout1)



        # Bind each button to a different function that prints a message
        button1.bind(on_press=self.go_to_test_page_1)
        button2.bind(on_press=self.go_to_test_page_2)


    def go_to_test_page_1(self, instance):
        print('Going to Test Page 1')

    def go_to_test_page_2(self, instance):
        print('Going to Test Page 2')



class MyApp(App):
    def build(self):
        layout = MyBoxLayout()
        window_width = 2 * 300 + 3 * 10 + 20
        window_height = 2 * 200 + 20
        self.window_size = (window_width, window_height)
        return layout

    def on_start(self):
        self.root_window.size = self.window_size

if __name__ == '__main__':
    MyApp().run()
