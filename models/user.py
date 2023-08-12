#!/usr/bin/python3
"""
module contains user and its instances
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Identifying the class User and it's
    Basic attributes
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        Initiate class and inherits from BaseModel
        """
        super().__init__(*args, **kwargs)
    