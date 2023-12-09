#!/usr/bin/python3
from models.review import Review
import unittest
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ test class for review """
    def test_review_attributes(self):
        """ tests for reviev attributes """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
