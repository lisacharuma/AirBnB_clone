#!/usr/bin/python3
import unittest
import os
import json
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Reset the storage before each test """
        storage.reload()

    def test_create_and_save_model(self):
        """ Create a new object """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        """ Reload objects and check if the created model is present """
        reloaded_objects = storage.all()
        self.assertIn(my_model, reloaded_objects.values())

    def test_file_path_attribute(self):
        """
        Test if FileStorage class has the __file_path attribute
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_objects_attribute(self):
        """
        Test if FileStorage class has the __objects attribute
        """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_all_method_exists(self):
        """
        Test if FileStorage class has the all method
        """
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(callable(getattr(FileStorage, 'all')))

    def test_all_returns_objects_dictionary(self):
        """
        Test if the all method returns the dictionary __objects
        """
        fs = FileStorage()
        all_objects = fs.all()
        self.assertEqual(all_objects, fs._FileStorage__objects)

    def test_new_method_exists(self):
        """
        Test if FileStorage class has the new method
        """
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(callable(getattr(FileStorage, 'new')))

    def test_new_sets_object_in_objects_dictionary(self):
        """
        Test if the new method sets the object in the
        __objects dictionary with key <obj class name>.id
        """
        fs = FileStorage()

        # Create a BaseModel instance
        my_model = BaseModel()

        # Call the new method
        fs.new(my_model)

        # Expected key in __objects dictionary
        expected_key = "{}.{}".format(my_model.__class__.__name__, my_model.id)

        # Check if the key is present in __objects
        self.assertIn(expected_key, fs._FileStorage__objects)

        # Check if the value associated with the key is the same as the object
        self.assertEqual(fs._FileStorage__objects[expected_key], my_model)

    def test_save_method_exists(self):
        """
        Test if FileStorage class has the save method
        """
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(callable(getattr(FileStorage, 'save')))

    def test_save_serializes_objects_to_json_file(self):
        """
        Test if the save method serializes __objects to the
        JSON file at __file_path
        """
        fs = FileStorage()

        # Create a BaseModel instance
        my_model = BaseModel()

        # Call the new method
        fs.new(my_model)

        # Call the save method
        fs.save()

        # Read the contents of the JSON file
        with open(fs._FileStorage__file_path, 'r') as file:
            file_contents = json.load(file)

        # Expected key in the serialized JSON
        expected_key = "{}.{}".format(my_model.__class__.__name__, my_model.id)

        # Check if the key is present in the serialized JSON
        self.assertIn(expected_key, file_contents)

        """
        Check if the value associated with the key in the serialized
        JSON is the same as the object's to_dict()
        """
        self.assertEqual(file_contents[expected_key], my_model.to_dict())

    def test_reload_method_exists(self):
        """
        Test if FileStorage class has the reload method
        """
        self.assertTrue(hasattr(FileStorage, 'reload'))
        self.assertTrue(callable(getattr(FileStorage, 'reload')))


if __name__ == '__main__':
    unittest.main()
