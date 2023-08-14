#!/usr/bin/env python3
"""Unittest for base_model"""

import unittest
import models.base_model
from models.base_model import BaseModel
from datetime import datetime as dt
import uuid
import os


class TestBaseModel(unittest.TestCase):
    """unitest class BaseModel"""

    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Jeffry"
        cls.base1.my_number = 69

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def reRunSet(self):
        """rerun"""
        pass

    def basemodel_test_docstrings(self):
        """Test: models.base_model module for documentation"""
        self.assertIsNotNone(models.base_model.__doc__)

    def basemodel_test_method_docs(self):
        """Test: methods in BaseModel for documentation"""
        methods = [
            BaseModel.__init__,
            BaseModel.__str__,
            BaseModel.save,
            BaseModel.to_dict,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def basemodel_test_class_doc(self):
        """Test: BaseModel class for documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def basemodel_test_functions_check(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def basemodel_test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def basemodel_test_init_attribute(self):
        """Test: basemodel id"""
        test_model = BaseModel()
        test_model2 = BaseModel()
        self.assertTrue(hasattr(test_model, "id"))
        self.assertIsNotNone(test_model.id)
        self.assertIsInstance(test_model.id, str)
        self.assertTrue(uuid.UUID(test_model.id))
        self.assertNotEqual(test_model.id, test_model2.id)
        self.assertTrue(hasattr(test_model, "created_at"))
        self.assertIsNotNone(test_model.created_at)
        self.assertIsInstance(test_model.created_at, dt)
        self.assertTrue(hasattr(test_model, "updated_at"))
        self.assertIsNotNone(test_model.updated_at)
        self.assertIsInstance(test_model.updated_at, dt)
        self.assertTrue(hasattr(test_model, "__class__"))
        self.assertIsNotNone(test_model.__class__)
        self.assertIsInstance(test_model.__class__, object)
        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)
        str_ = f"[BaseModel] ({test_model.id}) {test_model.__dict__}"
        self.assertEqual(str(test_model), str_)
        old = test_model.updated_at
        test_model.save()
        self.assertGreater(test_model.updated_at, old)

    def basemodel_test_kwargs_input(self):
        """Test: BaseModel: kwargs init"""
        dic = {
            "id": "apocalypse_preper-id-01",
            "created_at": "2009-08-09T12:34:56.789012",
            "updated_at": "2019-08-09T13:45:12.345678",
            "name": "Thomas",
            "value": 31,
        }
        test_model = BaseModel(**dic)
        self.assertEqual(test_model.id, "test_id")
        self.assertEqual(test_model.name, "Thomas")
        self.assertEqual(test_model.value, 31)
        self.assertIsInstance(test_model.created_at, dt)
        self.assertIsInstance(test_model.updated_at, dt)

    def basemodel_test_to_dict_data_type(self):
        """Test: data types after to_dict"""
        test_model = BaseModel()
        test_model.name = "henrey"
        test_model.num = 29
        test_model.age = "69"
        test_model.bool_val = True
        test_model.float_num = 29.99
        test_dict = test_model.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(test_dict["id"], test_model.id)
        self.assertEqual(test_dict["num"], 29)
        self.assertEqual(test_dict["name"], "henrey")
        self.assertEqual(test_dict["age"], "69")
        self.assertEqual(test_dict["bool_val"], True)
        self.assertEqual(test_dict["float_num"], 29.99)


if __name__ == "__main__":
    unittest.main()
