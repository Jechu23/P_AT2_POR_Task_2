from letter import Letter
"""Define the clas Letterbox"""


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
    def check_for_new_letters(self, key):
        unread_letters = self.get_unread_letters()
        for letter in unread_letters:
            print(f'From: {letter.sender}\nTo: {letter.recipient}\nContent:{letter.get_contents(key)}')
            letter.mark_read()