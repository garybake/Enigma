import string
import random

class Rotor:
    def __init__(self, start):
        self.mapping = {key: key for (key) in string.ascii_uppercase}  # default to A => A
        self.state = start

    def randomise_mappings(self):
        atoz = list(string.ascii_uppercase)
        random.shuffle(atoz)
        for key, value in enumerate(self.mapping):
            self.mapping[value] = atoz[key]

    def set_mappings(self, mappings=None):
        """
        TODO: what is the real order?
        - Cannot map to self
        """
        if mappings:
            self.mappings = mappings

    def map_letter(self, letter, reverse=False):
        """
        Get the letter mapping
        Use reverse=True for a reverse mapping
        """
        if not reverse:
            return self.mapping[letter]

        for key, val in self.mapping.items():
            if val == letter:
                return key
        return 'ERROR' # TODO
