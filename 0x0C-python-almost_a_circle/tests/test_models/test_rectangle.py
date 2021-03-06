#!/usr/bin/python3
"""Unit Tests for class Base"""
import unittest
from models.rectangle import Rectangle


class TestsRectangle(unittest.TestCase):

    def test_id(self):
        b1 = Rectangle(10, 2)
        self.assertEqual(b1.width, 10)
        b2 = Rectangle(2, 10)
        self.assertEqual(b2.height, 10)
        b3 = Rectangle(10, 2, 0, 0, 89)
        self.assertEqual(b3.id, 89)
        self.assertEqual(b3.x, 0)
        self.assertEqual(b3.y, 0)
        b1.x = 5
        self.assertEqual(b1.x, 5)
        b2.y = 9
        self.assertEqual(b2.y, 9)

    def test_valuesError(self):
        self.assertRaises(TypeError, Rectangle, (10, 2.8))
