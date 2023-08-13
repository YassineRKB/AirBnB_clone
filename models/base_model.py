#!/usr/bin/python3
"""base model class module"""

import models
from datetime import datetime as dt
from uuid import uuid4 as ids


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """constructor for basemodel class"""
        if not kwargs:
            self.id = str(ids())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if "__class__" == key:
                    pass
                elif "created_at" == key:
                    self.created_at = dt.strptime(
                        kwargs["created_at"],
                        "%Y-%m-%dT%H:%M:%S.%f"
                        )
                elif "updated_at" == key:
                    self.updated_at = dt.strptime(
                        kwargs["updated_at"],
                        "%Y-%m-%dT%H:%M:%S.%f"
                        )
                else:
                    setattr(self, key, val)

    def __str__(self):
        """representation of baseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """ returns representation string"""
        return (self.__str__())

    def save(self):
        """Save Method to save the instance"""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """instance attributes as dictionary"""
        the_dict = self.__dict__.copy()
        the_dict["__class__"] = type(self).__name__
        the_dict["updated_at"] = the_dict["updated_at"].isoformat()
        the_dict["created_at"] = the_dict["created_at"].isoformat()
        return the_dict
