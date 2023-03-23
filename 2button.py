import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from smartcard.System import readers

class RFIDReaderApp(App):

    def build(self):
        # Create a vertical box layout
        layout = BoxLayout(orientation='vertical')

        # Create a label widget
        self.rfid_label = Label(text="Scan RFID card...")

        # Create a button widget
        read_button = Button(text='Read RFID')

        # Bind the button to the read_rfid method
        read_button.bind(on_press=self.read_rfid)

        # Create another button widget
        image_button = Button(text='Show Image')

        # Bind the button to the display_image method
        image_button.bind(on_press=self.display_image)

        # Add the label and buttons to the layout
        layout.add_widget(self.rfid_label)
        layout.add_widget(read_button)
        layout.add_widget(image_button)

        return layout

    def read_rfid(self, instance):
        # Get a list of all available readers
        reader_list = readers()
        if len(reader_list) == 0:
            self.rfid_label.text = "No readers found"
            return

        # Connect to the first reader
        reader = reader_list[0]
        connection = reader.createConnection()
        connection.connect()

        # Send a command to the RFID card
        command = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        response, sw1, sw2 = connection.transmit(command)

        # Display the response from the RFID card
        if sw1 == 0x90:
            # Extract card information from response
            uid = ''.join('{:02X}'.format(x) for x in response)
            card_info = 'UID: ' + uid

            self.rfid_label.text = card_info
            print(card_info)
        else:
            self.rfid_label.text = "Failed to read RFID card"
            print("Failed to read RFID card")

    def display_image(self, instance):
        # Create an image widget
        image = Image(source='myimage.png')

        # Create a box layout for the image
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(image)

        # Create a popup window to display the image
        popup = popup(title='My Image', content=layout, size_hint=(0.8, 0.8))
        popup.open()

if __name__ == "__main__":
    RFIDReaderApp().run()
