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
        return "str"
    
    def save(self):
        return "saved"
    
    def to_dic(self):
        return "to dict"
    