#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_is_str(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

if __name__ == "__main__":
    unittest.main()
