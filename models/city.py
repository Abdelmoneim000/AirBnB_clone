#!/usr/bin/python3
"""
A module that contains City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Identifying City class and it's attribute:
    @state_id: holds a string of the id of the state.
    @name: name of the City.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initiate class and inherits from BaseModel
        """
        super().__init__(*args, **kwargs)
