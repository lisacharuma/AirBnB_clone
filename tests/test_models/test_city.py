#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    test the city class
    """

    def test_city_attributes(self):
        """
        test if city inherits from BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_if_state_id(self):
        """
        Test if attribute state_id is present
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))

    def test_if_name_is(self):
        """
        Test if attribute name is present
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))

    def test_if_state_id_is_empty(self):
        """
        test is stade id is empty string
        """
        city = City()
        self.assertEqual(city.state_id, "")

    def test_if_name_is_empty(self):
        """
        test name is empty string
        """
        city = City()
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
