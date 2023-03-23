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
        button1 = Button(text="Display Pic", on_press=self.show_image)
        button2 = Button(text="Display 2 button", on_press=self.duplicate_card)
        layout.add_widget(button1)
        layout.add_widget(button2)
        main_screen.add_widget(layout)
        sm.add_widget(main_screen)

        # Create the RFID screen
        duplicate_screen = Screen(name='Duplicate')
        layout = BoxLayout(orientation='vertical')
        button_read_AC = Button(text="Read Access Card", on_press=self.read_card)
        button_write_AC = Button(text="Write to new Access Card")
        button_backToMain = Button(text="back", on_press=self.back_toMain)
        layout.add_widget(button_read_AC)
        layout.add_widget(button_write_AC)
        layout.add_widget(button_backToMain)
        duplicate_screen.add_widget(layout)
        sm.add_widget(duplicate_screen)

        #Page for reading access card
        read_access_card_screen = Screen(name='Read_card')
        layout = BoxLayout(orientation='vertical')
        button_read = Button(text="Read Access Card")
        button_back = Button(text="back", on_press=self.back_toMain)
        layout.add_widget(button_read)
        layout.add_widget(button_back)
        read_access_card_screen.add_widget(layout)
        sm.add_widget(read_access_card_screen)


        return sm

    def back_toMain(self, instance):
        # Switch to the RFID screen
        self.root.current = 'main'

    def show_image(self, instance):
        # Create a popup window
        popup = Popup(title='My Image', size_hint=(None, None), size=(400, 400))
        image = Image(source='image.jpg')
        popup.add_widget(image)
        popup.open()

    def duplicate_card(self, instance):
        # Switch to the duplicate screen
        self.root.current = 'Duplicate'


    def read_card(self, instance):
        # Switch to the RFID screen
        self.root.current = 'Read_card'



        
if __name__ == '__main__':
    MyApp().run()
