#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_attributes(self):
        """ test if attributes are present """
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_id_is_str(self):
        """ test is id is string """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)

    def test_save_method(self):
        """ test save method """
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(initial_updated_at, self.my_model.updated_at)

    def test_for_uuid(self):
        """ tests if uuid is unique """
        my_model = BaseModel()
        my_uuid = str(uuid.uuid4())
        self.assertNotEqual(my_model.id, my_uuid)

    def test_created_at_type(self):
        """ test if created_at is datetime """
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_created_at_in_dict(self):
        """ test if created at is in dict """
        obj_dict = self.my_model.to_dict()
        self.assertTrue('created_at' in obj_dict)

    def test_updated_at(self):
        """ test if updated_at is in dict """
        obj_dict = self.my_model.to_dict()
        self.assertTrue('updated_at' in obj_dict)

    def test_class(self):
        """ test is class is in dictionary """
        obj_dict = self.my_model.to_dict()
        self.assertTrue('__class__' in obj_dict)

    def test_str_method(self):
        str_representation = str(self.my_model)
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn("({})".format(self.my_model.id), str_representation)


if __name__ == "__main__":
    unittest.main()
