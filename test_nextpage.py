from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def build(self):
        # Create a ScreenManager
        sm = ScreenManager()

        # Create the main screen
        main_screen = Screen(name='main')
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text="Press Me 1", on_press=self.show_image)
        button2 = Button(text="Press Me 2", on_press=self.read_rfid)
        layout.add_widget(button1)
        layout.add_widget(button2)
        main_screen.add_widget(layout)
        sm.add_widget(main_screen)

        # Create the RFID screen
        rfid_screen = Screen(name='rfid')
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text="Button 1")
        button2 = Button(text="Button 2")
        layout.add_widget(button1)
        layout.add_widget(button2)
        rfid_screen.add_widget(layout)
        sm.add_widget(rfid_screen)

        return sm

    def show_image(self, instance):
        # Create a popup window
        popup = Popup(title='My Image', size_hint=(None, None), size=(400, 400))
        image = Image(source='image.jpg')
        popup.add_widget(image)
        popup.open()

    def read_rfid(self, instance):
        # Switch to the RFID screen
        self.root.current = 'rfid'

        
if __name__ == '__main__':
    MyApp().run()
