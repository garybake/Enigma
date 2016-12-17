#!/usr/bin/env python3

from rotor_group import RotorGroup
import unittest

class RotorTest(unittest.TestCase):

    def setUp(self):
        self.rgroup = RotorGroup()

    def test_default_set(self):
        self.assertEqual(len(self.rgroup.rotors), 3)

        first_rotor = self.rgroup.rotors[0]
        self.assertEqual(first_rotor.state, 'A')

        third_rotor = self.rgroup.rotors[2]
        self.assertEqual(third_rotor.state, 'C')

if __name__ == '__main__':
    unittest.main()