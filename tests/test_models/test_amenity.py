#!/usr/bin/python3
"""
Amenity Tests
"""
import unittest
from models.amenity import Amenity


class MyTestCase(unittest.TestCase):
    """
    Amenity place class
    """
    def test_init(self):
        """
        init test
        """
        am = Amenity()
        self.assertIsInstance(am, Amenity)


if __name__ == '__main__':
    unittest.main()
