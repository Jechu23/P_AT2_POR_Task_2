"""Define the class Person in this case Alice and Bob"""
# Import Letterbox
from letterbox import Letterbox
from letter import Letter
from postoffice import Postoffice

class Person:
    # method initializes a new Person instance with a given name, Letterbox instance to store as an attribute.
    def __init__(self, name):
        self.name = name
        self.letterbox = Letterbox()



    def write_letter(self, recipient, contents):
        letter = Letter(self.name, recipient.name, contents)
        encrypted_message = letter.contents
        encrypted_letter = Letter(self.name, recipient.name, encrypted_message)
        Postoffice.send_letter(encrypted_letter)

    def read_letters(self, key):
        self.letterbox.check_for_new_letters(key)

