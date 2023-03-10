from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        # Create a button with a callback function
        button = Button(text="Press Me", on_press=self.show_image)

        return button

    def show_image(self, instance):
        # Create a popup window
        popup = Popup(title='My Image', size_hint=(None, None), size=(400, 400))

        # Create an image widget
        image = Image(source='index.jpg')

        # Add the image widget to the popup
        popup.add_widget(image)

        # Open the popup
        popup.open()

if __name__ == '__main__':
    MyApp().run()