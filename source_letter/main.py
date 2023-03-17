"""
Name: Jesus Huanambal
ID: 20096888
Date: 17/03/2023
Assessment : Part AT2 Task 2
"""

import time
from person import Person
""" The main.py file is where the Person instances are created and the program is run."""

if __name__ == '__main__':
    # Create letterboxes for Alice and Bob
    alice = Person('Alice')
    bob = Person('Bob')
    # Send another letter after 2 seconds
    time.sleep(2)
    # Create letters to send between Alice and Bob
    alice.write_letter(bob, 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n')
    bob.write_letter(alice, 'Hi Alice, I am great, thank you for asking!.\nsee ya!\nBob\n')

    # Alice and Bob check their letterboxes.
    while True:
        bob.read_letters()
        # Wait for 5 seconds before checking again
        time.sleep(5)
        alice.read_letters()
        break

