from rotor import Rotor

class RotorGroup:
    def __init__(self, initial_states=None):

        if not initial_states:
            initial_states = ['A', 'B', 'C']

        self.rotors = []
        rotor_count = len(initial_states)
        for i in range(rotor_count):
            r = Rotor(initial_states[i])
            self.rotors.append(r)
