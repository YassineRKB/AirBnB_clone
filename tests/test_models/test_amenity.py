#!/usr/bin/env python3
"""Unittest amenity module"""
import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenity(unittest.TestCase):
    """ unitest Amenity class"""

    def test_amenity_check_attribute(self):
        """Test: attribute check"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(type(amenity.name) == str)

    def test_amenity_class_doc(self):
        """Test: class has documentaion"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity_module_doc(self):
        """Test: module has documentation"""
        self.assertIsNotNone(models.amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
