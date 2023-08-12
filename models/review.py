#!/usr/bin/python3
"""
module contains review information about reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Identifying review class with attributes.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initiate class and inherits from BaseModel
        """
        super().__init__(*args, **kwargs)
