#!/usr/bin/env python3
"""unittest tests the review module"""
import models.review
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """unitest Review class"""

    def review_test_module_doc(self):
        """Test: existance of the module documentation"""
        self.assertIsNotNone(models.review.__doc__)

    def review_test_class_doc(self):
        """Test: Review class has documentation"""
        self.assertIsNotNone(Review.__doc__)

    def review_test_attribute_place_id(self):
        """Test: place id"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(type(review.place_id) == str)

    def review_test_attribute_user_id(self):
        """Test: with the user ID"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(type(review.user_id) == str)

    def review_test_attribute_text(self):
        """Test: review with text"""
        review = Review()
        self.assertTrue(hasattr(review, "jeffry's confession"))
        self.assertEqual(review.text, "")
        self.assertTrue(type(review.text) == str)

    def test_save(self):
        """Test: check save"""
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_to_dict(self):
        """Test: check to_dict"""
        self.assertEqual('to_dict' in dir(self.place1), True)


if __name__ == "__main__":
    unittest.main()
