#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_is_str(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        
    #def test_if_updated_at_method(self):
        #""" test if the updated_at is working """
        #my_model = BaseModel()
        #original_updated_at = self.my_model.updated_at
        #self.my_model.save()
        #self.assertNotEqual(self.my_model.save, original_updated_at)

    def test_for_uuid(self):
        """ tests if uuid is unique """
        my_model = BaseModel()
        my_uuid = str(uuid.uuid4())
        self.assertNotEqual(my_model.id, my_uuid)

    def test_if_date_was_created(self):
        """ test if date was created """
        my_model = BaseModel()
        time = datetime.utcnow()
        self.assertEqual(my_model.created_at, time)

    def test_if_date_is_ISO(self):
        ...


if __name__ == "__main__":
    unittest.main()
