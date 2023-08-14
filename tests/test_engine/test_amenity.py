#!/usr/bin/env python3
"""Unittest amenity module"""

import unittest
from models.amenity import Amenity
import models.amenity


class TestAmenity(unittest.TestCase):
    """ unitest Amenity class"""

    def amenity_test_check_attribute(self):
        """Test: attribute check"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
        self.assertTrue(type(amenity.name) == str)

    def amenity_test_class_doc(self):
        """Test: class has documentaion"""
        self.assertIsNotNone(Amenity.__doc__)

    def amenity_test_module_doc(self):
        """Test: module has documentation"""
        self.assertIsNotNone(models.amenity.__doc__)

    def amenity_test_save(self):
        """Test: check save"""
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def amenity_test_to_dict(self):
        """Test: check to_dict"""
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
