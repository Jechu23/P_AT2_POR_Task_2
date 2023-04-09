"""Define the class Letter"""


class Letter:
    # Initialization the class
    def __init__(self, sender, recipient, contents):
        self.sender = sender
        self.recipient = recipient
        self.contents = self.encrypt(contents)
        self.is_read = False

    # Mark the letter as read
    def mark_read(self):
        self.is_read = True

    # Mark the letter as unread
    def mark_unread(self):
        self.is_read = False

    def encrypt(self, message):
        encrypted = ''
        for char in message:
            encrypted += chr(ord(char)+1)
        return encrypted

    def decrypt(self, message, key):
        decrypt = ''
        for char in message:
            decrypt += chr(ord(char) - key)
        return decrypt

    def get_contents(self, key):
        return self.decrypt(self.contents, key)

