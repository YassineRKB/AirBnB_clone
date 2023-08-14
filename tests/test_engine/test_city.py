#!/usr/bin/env python3
"""Unittest for city class"""
import unittest
from models.city import City
import models.city


class TestCity(unittest.TestCase):
    """unitest City class"""

    def city_test_attributes_check(self):
        """Test: attr check"""
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)

    def city_test_attribut_state_id(self):
        """Test: attr with state id"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(type(city.state_id) == str)

    def city_test_attribut_name(self):
        """Test: attr with state name"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(type(city.name) == str)

    def city_test_class_doc(self):
        """Test: city documentation"""
        self.assertIsNotNone(City.__doc__)

    def city_test_module_doc(self):
        """Test: city module has documentation"""
        self.assertIsNotNone(models.city.__doc__)


if __name__ == "__main__":
    unittest.main()
