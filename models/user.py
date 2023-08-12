#!/usr/bin/python3
"""
module contains user and its instances
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
       class controlling user details
       inherits from BaseModel class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """ construct method
            called every time new
            instance created
        """
        super().__init__(*args, **kwargs)
    