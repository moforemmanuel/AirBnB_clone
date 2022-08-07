#!/usr/bin/python3
"""
City Tests
"""
import unittest
from models.city import City


class MyTestCase(unittest.TestCase):
    """
    City test class
    """
    def test_init(self):
        """
        init test
        """
        city = City()
        self.assertIsInstance(city, City)


if __name__ == '__main__':
    unittest.main()
