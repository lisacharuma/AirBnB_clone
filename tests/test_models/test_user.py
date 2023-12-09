#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.user = User(email="airbnb@mail.com", password="root", first_name="Betty", last_name="Bar")

    def test_user_to_dict(self):
        # Test if to_dict method of User returns a dictionary with correct attributes
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_user_attributes(self):
        """
        Test if User class inherits from BaseModel and has the specified attributes
        """
        self.assertIsInstance(self.user, User)

    def test_if_email_is_there(self):
        """ tests if attribute email is present """

        self.assertTrue(hasattr(self.user, "email"))

    def test_if_password_is_there(self):
        """ tests if attribute password is present """
        self.assertTrue(hasattr(self.user, "password"))

    def test_if_first_name_is_there(self):
        """ tests if attribute first_name is present """
        self.assertTrue(hasattr(self.user, "first_name"))

    def test_if_last_name_is_there(self):
        """ tests is attribute last_name is present """
        self.assertTrue(hasattr(self.user, "last_name"))

if __name__ == "__main__":
    unittest.main()
    
