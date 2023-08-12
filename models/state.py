#!/usr/bin/python3
"""
Module that contains the State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Identifying State class with it's attributes.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiate class and inherits from BaseModel
        """
        super().__init__(*args, **kwargs)
