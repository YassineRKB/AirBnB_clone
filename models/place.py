#!/usr/bin/python3
"""place class module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """place class"""

    name = ""
    city_id = ""
    user_id = ""
    amenity_ids = []
    longitude = 0.0
    latitude = 0.0
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
