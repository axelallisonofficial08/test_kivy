from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        # Create a layout to hold the buttons
        layout = BoxLayout(orientation='vertical')

        # Create the first button with a callback function
        button1 = Button(text="Press Me 1", on_press=self.show_image)

        # Create the second button with a different callback function
        button2 = Button(text="Press Me 2", on_press=self.show_message)

        # Add both buttons to the layout
        layout.add_widget(button1)
        layout.add_widget(button2)

        return layout

    def show_image(self, instance):
        # Create a popup window
        popup = Popup(title='My Image', size_hint=(None, None), size=(400, 400))

        # Create an image widget
        image = Image(source='image.jpg')

        # Add the image widget to the popup
        popup.add_widget(image)

        # Open the popup
        popup.open()

    def show_message(self, instance):
        # Create a popup window
        popup = Popup(title='My Message', size_hint=(None, None), size=(400, 400))

        # Create a label widget
        label = Label(text='Hello, world!')

        # Add the label widget to the popup
        popup.add_widget(label)

        # Open the popup
        popup.open()

if __name__ == '__main__':
    MyApp().run()
