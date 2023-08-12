#!/usr/bin/python3
"""
Module to set the storage of the
program
"""
import json
import datetime
import os
from models.user import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    A class to serialize instances to a JSON file
    and deserializes JSON file to instances.

    __file_path: the path to the json file which
    will be created.

    __objects: will store the objects id.
    """
    __file_path = "serial.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to JSON file,
        Using __file_path.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the file exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    self.__objects[key] = class_(**value)
