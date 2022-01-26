#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(max_integer([1, 2, 3, 6, 5]), 6)
        self.assertEqual(max_integer([]), None)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, 12)

    def test_string(self):
        self.assertEqual(max_integer("Hello world"), "w")

    def test_bool(self):
        self.assertEqual(max_integer([False, False, True]), True)

    def test_listdiverse(self):
        self.assertRaises(TypeError, max_integer, [3, False, "True", 14.4])
