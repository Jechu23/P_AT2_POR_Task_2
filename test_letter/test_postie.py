""" Unit Text for Mail Delivery """
# Import classes to use Unit text
from person import Person
from letter import Letter
from postie import Postie
import unittest


# Class Unit Text
class TestPostie(unittest.TestCase):
    # Create a test
    def test_postie_delivery(self):
        # Create Alice, Bob, and a Postie with a route to Bob's letterbox
        alice = Person('Alice')
        bob = Person('Bob')
        postie = Postie({'Bob': bob})

        # Alice writes a letter to Bob and drops it off at the Post Office
        message = 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n'
        encrypted_message = Letter('Alice', 'Bob', message).contents
        alice.write_letter(bob, encrypted_message)

        # Postie picks up the letter from the Postoffice and delivers it to Bob's letterbox
        postie.deliver_mail()

        # Bob checks his letterbox
        bob_letters = bob.letterbox.get_unread_letters()

        # Assert that Bob received the letter
        self.assertEqual(len(bob_letters), 1)
        self.assertEqual(bob_letters[0].sender, 'Alice')
        self.assertEqual(bob_letters[0].recipient, 'Bob')


if __name__ == '__main__':
    unittest.main()


