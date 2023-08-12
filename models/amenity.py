#!/usr/bin/python3
"""
module contains amenity information and its methods
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class with amenity information
    inherits from BaseModel class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method
           being called everytime
           new instance create
        """
        super().__init__(*args, **kwargs)
