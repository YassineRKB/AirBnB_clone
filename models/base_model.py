#!/usr/bin/python3
"""base model class module"""

import models
from models import storage
from datetime import datetime as dt
from uuid import uuid4 as ids


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """constructor for basemodel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "id":
                        setattr(self, key, str(value))
                    elif key == "updated_at" or "created_at":
                        dateFormat = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, dt.strftime(value, dateFormat))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(ids())
            self.created_at = dt.now()
            self.updtaed_at = dt.now()
            storage.new(self)

    def __str__(self):
        """representation of baseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """ returns representation string"""
        return (self.__str__())

    def save(self):
        """Save Method to save the instance"""
        self.updtaed_at = dt.now()
        storage.save()

    def to_dic(self):
        """instance attributes as dictionary"""
        the_dict = self.__dict__.copy()
        the_dict.update({"__class__": self.__class__.__name__})
        the_dict.update({"created_at": str(self.created_at.isoformat())})
        the_dict.update({"updated_at": str(self.updtaed_at.isoformat())})
        return the_dict
