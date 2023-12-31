#!/usr/bin/python3
"""unitest model for user"""
import os
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """unitest userClass"""

    @classmethod
    def setUpClass(cls):
        """Test: init user"""
        cls.my_user = User()
        cls.my_user.first_name = "Jeffry"
        cls.my_user.last_name = "Epstieb"
        cls.my_user.email = "Epstien@lolisland.evil"
        cls.my_user.password = "fancySteakMediumRareOnHellFire123"

    @classmethod
    def tearDownClass(cls):
        """Test: remove storage file"""
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_class_doc(self):
        """Test: for the class documentation"""
        self.assertIsNotNone(User.__doc__)

    def test_user_is_subclass(self):
        """Test: afferm is subclass"""
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_user_functions_check(self):
        """Test: check functions"""
        self.assertIsNotNone(User.__doc__)

    def test_user_attributes_check(self):
        """Test: check attr"""
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)

    def test_user_attributes_datatype(self):
        """Test: check attr data type"""
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)

    def test_user_check_save(self):
        """Test: check save"""
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_user_to_dict(self):
        """Test: to_dict check"""
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
