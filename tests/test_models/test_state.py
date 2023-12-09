#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
    test cases for State class
    """

    def test_state_attributes(self):
        """
        test if state inherits from BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_for_attribute_name(self):
        """
        test if name attribute is present in state class
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_if_state_name_is_empty(self):
        """
        empty string
        """
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
