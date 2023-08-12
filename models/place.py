#!/usr/bin/python3
"""
module contains place information about place.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that holds info about the location.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initiate class and inherits from BaseModel
        """
        super().__init__(*args, **kwargs)
