import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pyautogui

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        
        # Set the orientation of the BoxLayout to vertical
        self.orientation = 'vertical'
        
        # Create a horizontal BoxLayout for each row of buttons
        for i in range(2):
            row_layout = BoxLayout(size_hint=(None, None), height=200)
            row_layout.spacing = 10
            row_layout.padding = [10, 0, 10, 0]

            # Add two buttons to each row
            button1 = Button(text='Button 1', size_hint=(None, 1), width=300)
            button2 = Button(text='Button 2', size_hint=(None, 1), width=300)
            row_layout.add_widget(button1)
            row_layout.add_widget(button2)

            # Add the row layout to the main layout
            self.add_widget(row_layout)

class MyApp(App):
    def build(self):
        layout = MyBoxLayout()
        return layout

    def on_start(self):
        if self.root_window:
            # Get the size of the screen
            screen_width, screen_height = pyautogui.size()

            # Calculate the window size and position for a 16:9 aspect ratio
            window_width = int(screen_height * 16 / 9)
            window_height = screen_height
            window_x = int((screen_width - window_width) / 2)
            window_y = 0

            # Set the position and size of the app window
            self.root_window.position = (window_x, window_y)
            self.root_window.size = (window_width, window_height)

if __name__ == '__main__':
    MyApp().run()