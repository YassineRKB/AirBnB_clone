#!/usr/bin/python3
"""unitest for AirBnb clone: console"""
import json
import unittest
from unittest.mock import patch
import os
from io import StringIO
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """unitest for cmd interperter"""

    @classmethod
    def setUpClass(self):
        """initiating a class for testing"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove storage file"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def console_test_docstrings(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    """Test the outputs"""
    def console_test_emptyline(self):
        """Test empty user input"""
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("\n")
            self.assertEqual(capturedOutput.getvalue(), '')

    def console_test_all(self):
        """Test: command All output"""
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual(
                "** class doesn't exist **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", capturedOutput.getvalue())

    def console_test_create(self):
        """Test: command create output"""
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("create")
            self.assertEqual(
                "** class name missing **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("create SomeClass")
            self.assertEqual(
                "** class doesn't exist **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]", capturedOutput.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("create User")
            self.typing.onecmd("create User")

    def console_test_update(self):
        """Test command update output"""
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             capturedOutput.getvalue())

    def console_test_show(self):
        """Test command show output"""
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             capturedOutput.getvalue())
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n",
                             capturedOutput.getvalue())

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual(
                "** class doesn't exist **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n",
                capturedOutput.getvalue()
                )
        with patch('sys.stdout', new=StringIO()) as capturedOutput:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual(
                "** no instance found **\n",
                capturedOutput.getvalue()
                )


if __name__ == "__main__":
    unittest.main()
