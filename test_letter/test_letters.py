import unittest

from source_letter.send_letters import Person, Letter, Letterbox


class TestLetter(unittest.TestCase):

    def setUp(self):
        self.alice = Person('Alice')
        self.bob = Person('Bob')

    def test_mark_read(self):
        # Create a new letter object and mark it as read
        letter = Letter('Alice', 'Bob', 'Test content')
        letter.mark_read()
        # Check the is_read is True
        self.assertTrue(letter.is_read)

    def test_receive_letter(self):
        letter = Letter('Alice', 'Bob', 'tes content')
        letterbox = Letterbox()
        # Call receive_letter method as check
        letterbox.receive_letter(letter)
        self.assertIn(letter, letterbox.letters)


class TestLetterBox(unittest.TestCase):
    def setUp(self):
        self.alice = Person('Alice')
        self.bob = Person('Bob')

    def test_receive_letter(self):
        letter = Letter(self.alice.name, self.bob.name, 'Hello')
        self.bob.letterbox.receive_letter(letter)
        self.assertIn(letter, self.bob.letterbox.letters)

    def test_send_letter(self):
        letter = Letter(self.alice.name, self.bob.name, 'Hello')
        self.alice.letterbox.send_letter(self.bob.letterbox, letter)
        self.assertIn(letter, self.bob.letterbox.letters)
        self.assertTrue(letter.mark_unread)


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.alice = Person('Alice')
        self.bob = Person('Bob')

    def test_write_letter(self):
        # Alice write letter to Bob
        alice_message = 'Hi Bob, how are you mate?.\nWhats news?\nBye\nAlice\n'
        self.alice.write_letter(self.bob, alice_message)

        # check letters in the Bob Letterbox as unread
        unread_letters = self.bob.letterbox.get_unread_letters()
        self.assertEqual(len(unread_letters), 1)
        self.assertEqual(unread_letters[0].sender, 'Alice')
        self.assertEqual(unread_letters[0].recipient, 'Bob')
        self.assertEqual(unread_letters[0].contents, alice_message)
        self.assertFalse(unread_letters[0].is_read)

    def test_read_letters(self):
        # Bob write a message to Alice
        bob_message = 'Hi Alice, I am great, thank you for asking!.\nsee ya!\nBob\n'
        self.bob.write_letter(self.alice, bob_message)

        # check letters in the Alice Letterbox as unread
        unread_letters = self. alice.letterbox.get_unread_letters()
        self.assertEqual(len(unread_letters), 1)
        self.assertEqual(unread_letters[0].sender, 'Bob')
        self.assertEqual(unread_letters[0].recipient, 'Alice')
        self.assertEqual(unread_letters[0].contents, bob_message)
        self.assertFalse(unread_letters[0].is_read)

        # Alice reads her letter from Bob
        self.alice.read_letters()
