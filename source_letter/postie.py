import time
from postoffice import Postoffice
"""Posting delivering"""

class Postie:
    # Define the class constructor, parameter route,
    # When the new instance od the Postie class is created this constructor will be called automatically, and the route
    # parameter will be passed to it.
    def __init__(self, route):
        self.route = route

    # Method to deliver letter.
    def deliver_mail(self):
        for letter in Postoffice.get_letters():
            recipient = letter.recipient
            if recipient in self.route:
                recipient_letterbox = self.route[recipient].letterbox
                recipient_letterbox.receive_letter(letter)
