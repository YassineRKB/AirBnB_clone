#!/usr/bin/env python3
"""unittest tests the review module"""
import models.review
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """unitest Review class"""

    def test_review_module_doc(self):
        """Test: existance of the module documentation"""
        self.assertIsNotNone(models.review.__doc__)

    def test_review_class_doc(self):
        """Test: Review class has documentation"""
        self.assertIsNotNone(Review.__doc__)

    def test_review_attribute_place_id(self):
        """Test: place id"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(type(review.place_id) == str)

    def test_review_attribute_user_id(self):
        """Test: with the user ID"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(type(review.user_id) == str)

    def test_review_attribute_text(self):
        """Test: review with text"""
        review = Review()
        self.assertTrue(hasattr(review, "jeffry's confession"))
        self.assertEqual(review.text, "")
        self.assertTrue(type(review.text) == str)


if __name__ == "__main__":
    unittest.main()
