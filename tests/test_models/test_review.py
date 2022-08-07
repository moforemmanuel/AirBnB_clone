#!/usr/bin/python3
"""
Review Tests
"""
import unittest
from models.review import Review


class MyTestCase(unittest.TestCase):
    """
    Review test class
    """
    def test_init(self):
        """
        init test
        """
        rev = Review()
        self.assertIsInstance(rev, Review)


if __name__ == '__main__':
    unittest.main()
