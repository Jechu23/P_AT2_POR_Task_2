"""
Name: Jesus Huanambal
ID: 20096888
Date: 17/03/2023
Assessment : Part AT2 Task 2
"""

import time
from person import Person
from postie import Postie
from letter import Letter

""" The main.py file is where the Person instances are created and the program is run."""

if __name__ == '__main__':

    alice = Person('Alice')
    bob = Person('Bob')
    key = 1

    # Create a postie and assign a route
    postie = Postie({'Bob': bob})

    # Alice writes a letter to Bob and drops it off at the Post Office
    # alice.write_letter(bob, 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n')
    message = 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n'
    encrypted_message = Letter('Alice', 'Bob', message).contents
    alice.write_letter(bob, encrypted_message)

    # Postie picks up the letter from the Postoffice and delivers it to Bob's letterbox
    postie.deliver_mail()

    # Bob checks his letterbox
    bob.read_letters(key)


