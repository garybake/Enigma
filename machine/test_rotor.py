#!/usr/bin/env python3

import unittest

from rotor import Rotor
import map_set

class RotorTest(unittest.TestCase):

    def setUp(self):
        mapping = 'BCADEFGHIJKLMNOPQRSTUVWXYZ'
        r = Rotor(key_order=mapping, start_state='A')
        self.rtr = r

    def test_start_position(self):
        r = self.rtr
        self.assertEqual(r.state, 'A')
        self.assertEqual(r.key_order[0], 'B')
        self.assertEqual(r.key_order[3], 'D')


    def test_state(self):
        r = self.rtr
        self.assertEqual(r.state_index(), 0)

        r.set_state('D')
        self.assertEqual(r.state, 'D')
        self.assertEqual(r.state_index(), 3)

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