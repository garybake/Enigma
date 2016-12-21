#!/usr/bin/env python3

import unittest

from rotor_group import RotorGroup
import map_set

class RotorTest(unittest.TestCase):

    def setUp(self):
        self.rgroup = RotorGroup(map_set=map_set.MAP_SET_1294_COMMERCIAL)

    def test_default_set(self):
        self.assertEqual(len(self.rgroup.rotors), 3)

        first_rotor = self.rgroup.rotors[0]
        self.assertEqual(first_rotor.state, 'A')

        third_rotor = self.rgroup.rotors[2]
        self.assertEqual(third_rotor.state, 'A')

    def test_group_mapping(self):
        map_a = self.rgroup.map_letter('A')
        self.assertEqual(map_a, 'Z')

        # All set to default
        # for r in self.rgroup.rotors:
        #     print(r.key_order)

if __name__ == '__main__':
    unittest.main()