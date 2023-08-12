#!/usr/bin/python3
"""
Amenity module and it's methods
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Identify Amenity class and it's attributes:
    @name: name of the class.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiate a new instance and make it
        inheritis all attributes from baseModel
        Class.
        """
        super().__init__(*args, **kwargs)
