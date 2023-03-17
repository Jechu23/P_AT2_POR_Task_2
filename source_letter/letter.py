"""Define the class Letter"""


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