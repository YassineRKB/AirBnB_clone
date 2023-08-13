#!/usr/bin/python3
"""user class module"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""
    age = ""
