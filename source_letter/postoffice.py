

class Postoffice:
    # create an empty list
    letters = []
    # Python decorator to define class method in a Postoffice class
    @classmethod
    def send_letter(cls, letter):
        cls.letters.append(letter)

    # Python decorator to define class method in a Postoffice class
    @classmethod
    def get_letters(cls):
        letters = cls.letters
        cls.letters = []
        return letters
