#!/usr/bin/python3
"""
module contains review information and properties
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class for reviewing by users
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor method"""
        super().__init__(*args, **kwargs)
