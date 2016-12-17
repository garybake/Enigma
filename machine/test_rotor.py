#!/usr/bin/env python3

from rotor import Rotor
import unittest

class RotorTest(unittest.TestCase):

    def setUp(self):
        r = Rotor('A')
        new_mapping = r.mapping
        new_mapping['A'] = 'B'
        new_mapping['B'] = 'C'
        new_mapping['C'] = 'A'

        r.set_mappings(new_mapping)
        self.rtr = r

    def test_start_position(self):
        r1 = Rotor('A')
        self.assertEqual(r1.state, 'A')
        r2 = Rotor('R')
        self.assertEqual(r2.state, 'R')

    def test_letter_mapping(self):
        r = self.rtr
        self.assertEqual(r.map_letter('A'), 'B')
        self.assertEqual(r.map_letter('D'), 'D')
        self.assertEqual(r.map_letter('Z'), 'Z')

        self.assertEqual(r.map_letter('B', reverse=True), 'A')
        self.assertEqual(r.map_letter('D', reverse=True), 'D')
        self.assertEqual(r.map_letter('Z', reverse=True), 'Z')

if __name__ == '__main__':
    unittest.main()