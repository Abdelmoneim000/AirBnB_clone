#!/usr/bin/python3
"""
module contains state class and its methods
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    class that stores state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor method"""
        super().__init__(*args, **kwargs)
