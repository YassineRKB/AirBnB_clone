#!/usr/bin/python3
"""Storage Engine: file module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """FileStorage class file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """function to get dict of serialized obj"""
        return self.__objects

    def new(self, obj):
        """func to serialize a new obj"""
        index = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[index] = obj

    def save(self):
        """func to update json file with serialized objects"""
        to_save = {}
        for key, value in self.__objects.items():
            to_save[key] = value.to_dict()
        with open(self.__file_path, "w") as w:
            json.dump(to_save, w)

    def reload(self):
        """func to load data from file + create instances accordingly"""
        try:
            with open(self.__file_path) as r:
                data = json.load(r)
            for key, value in data.items():
                self.new(eval(key.split(".")[0])(**value))
        except FileNotFoundError:
            pass
