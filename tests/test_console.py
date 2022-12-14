#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def create(self, server=None):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_write(self, nr=None):
        """Returns last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Quit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """EOF"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_help(self):
        """help"""
        cli = self.create()
        self.assertTrue(cli.onecmd("help"))
        # self.assertEqual(cli.onecmd("help"), None)

    def test_default(self):
        """default"""
        cli = self.create()
        self.assertTrue(cli.onecmd("BaseModel.all()"))
        self.assertTrue(cli.onecmd("BaseModel.count()"))
        self.assertTrue(cli.onecmd("BaseModel.show(1234)"))
        self.assertTrue(cli.onecmd("BaseModel.destroy(1234)"))
        self.assertTrue(cli.onecmd('BaseModel.update(1234, name, "mofor")'))
        # self.assertEqual(cli.onecmd("BaseModel.all()"), None)
        # self.assertEqual(cli.onecmd("BaseModel.count()"), None)
        # self.assertEqual(cli.onecmd("BaseModel.show(1234)"), None)
        # self.assertEqual(cli.onecmd("BaseModel.destroy(1234)"), None)
        # self.assertEqual(cli.onecmd('BaseModel.update(1234, name, "mofor")'), None)


if __name__ == '__main__':
    unittest.main()
