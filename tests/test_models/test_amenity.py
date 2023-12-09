#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests for amenity attributes """
    def test_amenity_attributes(self):
        """ test the attributes """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
