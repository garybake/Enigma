
import random
import map_set

class Rotor:

    def __init__(self, key_order, start_state=None):
        """
        state is which character points to the first of the key order
        """
        self.identity_map = map_set.IDENTITY_MAP
        self.key_order = key_order

        if not start_state:
            start_state = self.identity_map[0]

        self.state = start_state


    def state_index(self):
        return self.identity_map.index(self.state)

    def set_state(self, state):
        self.state = state        

    def map_letter(self, letter, reverse=False):
        """
        Get the letter mapping
        Use reverse=True for a reverse mapping
        """
        if not reverse:
            idx = self.identity_map.index(letter) - self.state_index()
            if idx < 0:
                idx = idx + 26
            return self.key_order[idx]
        else:
            idx = self.key_order.index(letter) + self.state_index()
            if idx > 25:
                idx = idx - 26
            return self.identity_map[idx]
