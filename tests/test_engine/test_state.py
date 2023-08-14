#!/usr/bin/env python3
"""Unittest for state module"""
import unittest
from models.state import State
import models.state


class TestState(unittest.TestCase):
    """unitest State class"""

    def state_test_module_doc(self):
        """Test: module has documentation"""
        self.assertIsNotNone(models.state.__doc__)

    def state_test_class_doc(self):
        """Test: class has documentation"""
        self.assertIsNotNone(State.__doc__)

    def state_test_attribute_check(self):
        """Test: attr check"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")



if __name__ == "__main__":
    unittest.main()
