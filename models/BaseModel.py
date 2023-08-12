#!/usr/bin/python3
"""base model class module"""

from datetime import datetime as dt
from uuid import uuid4 as ids


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        "constructor for basemodel class"
        if not kwargs:
            self.id = str(ids())
            self.created_at = dt.now()
            self.updtaed_at = dt.now()
            ## engine.new.save
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "id":
                        setattr(self, key, str(value))
                    elif key == "updated_at" or "created_at":
                        dateFormat = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, dt.strftime(value, dateFormat))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """representation of baseModel class"""
        rep = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return rep
    
    def save(self):
        """Save Method to save the instance"""
        self.updtaed_at = dt.now()
        ## engine.save
    
    def to_dic(self):
        return "to dict"
    