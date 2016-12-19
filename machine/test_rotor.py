#!/usr/bin/env python3

import unittest

from rotor import Rotor
import map_set

class RotorTest(unittest.TestCase):

    def setUp(self):
        # mappi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.mapping = 'WXYZABCDEFGHIJKLMNOPQRSTUV'
        r = Rotor(key_order=self.mapping, start_state='A')
        self.rtr = r

    def test_start_position(self):
        r = self.rtr
        self.assertEqual(r.state, 'A')
        self.assertEqual(r.key_order[0], 'W')
        self.assertEqual(r.key_order[3], 'Z')

        r2 = Rotor(key_order=self.mapping)
        self.assertEqual(r2.state_index(), 0)

        r2 = Rotor(key_order=self.mapping, start_state='E')
        self.assertEqual(r2.state_index(), 4)

    def test_letter_mapping(self):
        r = self.rtr
        self.assertEqual(r.map_letter('A'), 'W')
        self.assertEqual(r.map_letter('D'), 'Z')
        self.assertEqual(r.map_letter('Z'), 'V')

        self.assertEqual(r.map_letter('A', reverse=True), 'E')
        self.assertEqual(r.map_letter('D', reverse=True), 'H')
        self.assertEqual(r.map_letter('Z', reverse=True), 'D')
        self.assertEqual(r.map_letter('W', reverse=True), 'A')

    def test_state(self):
        r = self.rtr
        self.assertEqual(r.state_index(), 0)

        r.set_state('D')
        # mapping_i = ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
        # mapping_m = TUVWXYZABCDEFGHIJKLMNOPQRSTUV'
        self.assertEqual(r.state, 'D')
        self.assertEqual(r.state_index(), 3)

        self.assertEqual(r.map_letter('G'), 'Z')
        self.assertEqual(r.map_letter('P'), 'I')
        self.assertEqual(r.map_letter('C'), 'V')

        self.assertEqual(r.map_letter('A'), 'T')
        self.assertEqual(r.map_letter('Z'), 'S')

        self.assertEqual(r.map_letter('T', reverse=True), 'A')
        self.assertEqual(r.map_letter('H', reverse=True), 'O')
        self.assertEqual(r.map_letter('S', reverse=True), 'Z')

        r.set_state('Z')
        # mapping_i = ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # mapping_m = WXYZABCDEFGHIJKLMNOPQRSTUVW'
        self.assertEqual(r.state, 'Z')
        self.assertEqual(r.state_index(), 25)

        self.assertEqual(r.map_letter('A'), 'X')
        self.assertEqual(r.map_letter('M'), 'J')
        self.assertEqual(r.map_letter('Z'), 'W')


if __name__ == '__main__':
    unittest.main()