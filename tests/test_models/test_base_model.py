#!/usr/bin/python3

"""
test base model
"""

import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime


class MyTestCase(unittest.TestCase):
    """
    Test for Base Model
    """
    def test_initialization(self):
        """
        test for init
        :return: test
        """
        base = BaseModel()
        self.assertIsInstance(base.id, UUID)  # add assertion here
        self.assertIsInstance(base.created_at, datetime)

    def test_of_to_dict(self):
        """
        test for to_dict()
        """
        base = BaseModel()
        dict_obj = base.to_dict()
        self.assertIsInstance(dict_obj, dict)

    def test_of_save(self):
        """
        test for save()
        """
        base = BaseModel()
        base.save()
        self.assertIsInstance(base.updated_at, datetime)




if __name__ == '__main__':
    unittest.main()
