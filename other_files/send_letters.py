
import time


# Define the Letter Class
class Letter:
    # Initialization the class
    def __init__(self, sender, recipient, contents):
        self.sender = sender
        self.recipient = recipient
        self.contents = contents
        self.is_read = False

    # Mark the letter as read
    def mark_read(self):
        self.is_read = True

    # Mark the letter as unread
    def mark_unread(self):
        self.is_read = False


# Define the Letterbox Class
class Letterbox:
    def __init__(self):
        # List to store letters
        self.letters = []

    # Receive a letter to store in the list.
    def receive_letter(self, letter):
        self.letters.append(letter)

    # Send the letter to another letterbox (alice or Bob)

    def send_letter(self, recipient_letterbox, letter):
        letter.mark_unread()
        recipient_letterbox.receive_letter(letter)

    # Get all unread letters in the letterbox.
    def get_unread_letters(self):
        return [letter for letter in self.letters if not letter.is_read]

    # Check for new letters in the letterbox, print them, and mark then as read.
    def check_for_new_letters(self):
        unread_letters = self.get_unread_letters()
        for letter in unread_letters:
            print(f'From: {letter.sender}\nTo: {letter.recipient}\nContent:{letter.contents}')
            letter.mark_read()


# Define Person class
class Person:
    def __init__(self, name):
        self.name = name
        self.letterbox = Letterbox()

    def write_letter(self, recipient, contents):
        letter = Letter(self.name, recipient.name, contents)
        self.letterbox.send_letter(recipient.letterbox, letter)

    def read_letters(self):
        self.letterbox.check_for_new_letters()


if __name__ == '__main__':

    # Create Person instances
    alice = Person('Alice')
    bob = Person('Bob')

    time.sleep(2)
    # Alice writes a letter to Bob
    alice.write_letter(bob, 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n')
    # Bod writes a letter back to Alice
    bob.write_letter(alice, 'Hi Alice, I am great, thank you for asking!.\nsee ya!\nBob\n')

    #  Alice and Bob check their letterboxes
    while True:
        bob.read_letters()
        time.sleep(5)
        alice.read_letters()
        break