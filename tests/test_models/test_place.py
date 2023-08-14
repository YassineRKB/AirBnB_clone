##!/usr/bin/python3
"""unitest place"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """unitest place"""

    def test_place_class_doc(self):
        """Test: Place class has documentaion"""
        self.assertIsNotNone(Place.__doc__)

    def test_place_is_subclass(self):
        """Test: assert if its a subclass"""
        self.assertTrue(issubclass(self.place1.__class__, BaseModel), True)

    def test_place_functions_check(self):
        """Test: check funcs"""
        self.assertIsNotNone(Place.__doc__)

    def test_place_attributes_check(self):
        """Test: check attr"""
        self.assertTrue('id' in self.place1.__dict__)
        self.assertTrue('city_id' in self.place1.__dict__)
        self.assertTrue('user_id' in self.place1.__dict__)
        self.assertTrue('name' in self.place1.__dict__)
        self.assertTrue('description' in self.place1.__dict__)
        self.assertTrue('number_rooms' in self.place1.__dict__)
        self.assertTrue('number_bathrooms' in self.place1.__dict__)
        self.assertTrue('max_guest' in self.place1.__dict__)
        self.assertTrue('price_by_night' in self.place1.__dict__)
        self.assertTrue('latitude' in self.place1.__dict__)
        self.assertTrue('amenity_ids' in self.place1.__dict__)
        self.assertTrue('longitude' in self.place1.__dict__)
        self.assertTrue('created_at' in self.place1.__dict__)
        self.assertTrue('updated_at' in self.place1.__dict__)

    def test_place_attributes_datatype(self):
        """Test: assert attr datatype"""
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)
        self.assertEqual(type(self.place1.longitude), float)


if __name__ == "__main__":
    unittest.main()
