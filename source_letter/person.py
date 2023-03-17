"""Define the class Person in this case Alice and Bob"""
# Import Letterbox
from letterbox import Letterbox


class Person:
    # method initializes a new Person instance with a given name, Letterbox instance to store as an attribute.
    def __init__(self, name):
        self.name = name
        self.letterbox = Letterbox()

    def write_letter(self, recipient, contents):
        from letter import Letter
        letter = Letter(self.name, recipient.name, contents)
        self.letterbox.send_letter(recipient.letterbox, letter)

    def read_letters(self):
        self.letterbox.check_for_new_letters()
