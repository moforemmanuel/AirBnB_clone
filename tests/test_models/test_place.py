#!/usr/bin/python3
"""
Place Tests
"""
import unittest
from models.place import Place


class MyTestCase(unittest.TestCase):
    """
    Place test class
    """
    def test_init(self):
        """
        init test
        """
        p = Place()
        self.assertIsInstance(p, Place)


if __name__ == '__main__':
    unittest.main()
