#!/usr/bin/python3
"""
Users Tests
"""
import unittest
from models.user import User


class MyTestCase(unittest.TestCase):
    """
    User test class
    """
    def test_init(self):
        """
        init test
        """
        user = User()
        self.assertIsInstance(user, User)
        # self.assertEqual(user.id, str)


if __name__ == '__main__':
    unittest.main()
