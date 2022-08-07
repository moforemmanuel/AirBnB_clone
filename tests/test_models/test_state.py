#!/usr/bin/python3
"""
State Tests
"""
import unittest
from models.state import State


class MyTestCase(unittest.TestCase):
    """
    State test class
    """
    def test_init(self):
        """
        init test
        """
        state = State()
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
