#! /usr/bin/env python
import unittest

from py_ros_test_example.example_lib import Counter

class TestCounter(unittest.TestCase):

    def test_default_constructor(self):
        c = Counter()
        self.assertEqual(c.get(), 0)

    def test_next(self):
        c = Counter()
        c.next()
        self.assertEqual(c.get(), 1)
        c.next()
        self.assertEqual(c.get(), 2)
        c.next()
        c.next()
        self.assertEqual(c.get(), 4)

    def test_previous(self):
        c = Counter()
        c.previous()
        self.assertEqual(c.get(), -1)
        c.previous()
        self.assertEqual(c.get(), -2)
        c.previous()
        c.previous()
        self.assertEqual(c.get(), -4)


if __name__ == '__main__':
    unittest.main()
