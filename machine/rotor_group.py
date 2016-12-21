from rotor import Rotor

class RotorGroup:

    def __init__(self, map_set, initial_states=None):
        rotor_count = len(map_set)
        if not initial_states:
            initial_states = ['A'] * len(map_set)

        self.rotors = []
        for idx in range(rotor_count):
            r = Rotor(key_order=map_set[idx], start_state='A')
            self.rotors.append(r)

    def map_letter(self, letter, reverse=False):
        """
        Get the letter mapping running through all of the rotors
        Use reverse=True for a reverse mapping
        """

        rotor_list = self.rotors
        if reverse:
            rotor_list = reversed(self.rotors)

        current_letter = letter
        for r in rotor_list:
            current_letter = r.map_letter(current_letter)
        return current_letter
