import json
import datetime
import os
"""
A module for serialization and deserialization
"""

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
        self.__objects.update({type(obj).__name__ : obj.id})
    
    def save(self):
        """
        serializes __objects to JSON file,
        Using __file_path.
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the file exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                new_obj = json.load(f)
                self.__objects = new_obj

