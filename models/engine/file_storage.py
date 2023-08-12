#!/usr/bin/python3
"""Storage Engine: file module"""

import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage class file"""

    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel
    }

    def all(self):
        """function to get dict of serialized obj"""
        return self.__objects

    def new(self, obj):
        """func to serialize a new obj"""
        typeobjName = type(obj).__name__
        key = f"{typeobjName}.{obj.id}"
        self.__objects[key] = obj

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
            with open(self.__file_path, "r") as r:
                data = json.load(r)
            for key, value in data.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
