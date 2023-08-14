#!/usr/bin/python3
"""Unittest FileStorage class"""
import unittest
from models.base_model import BaseModel
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """unitest file storage"""

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Imir castle"
        cls.rev1.user_id = "Von Saltok Bjorn"
        cls.rev1.text = "renov premium care pack"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_storage_new(self):
        """Test: new"""
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        klien = User()
        klien.id = 6969
        klien.name = "klien"
        m_storage.new(klien)
        key = klien.__class__.__name__ + "." + str(klien.id)
        self.assertIsNotNone(instances_dic[key])

    def test_storage_all(self):
        """Test: all (returns dictionary <class>.<id> : <obj instance>)"""
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_storage_reload(self):
        """Test: reload (reloads objects from string file)"""
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
