#!/usr/bin/python3
"""Unit Tests for class Base"""
import unittest
from models.base import Base


class TestsBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)
