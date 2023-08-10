"""
A model to define all base attributes and methods
"""

import uuid
import datetime
import models


class BaseModel():
    """
    A class to pass basic attributes
    """

    def __init__(self, *args, **kwargs):
        """
        Initiating an instance...

        id: identifier of the instance represented
        with numbers inside a string

        created_at: date of the instance in which it has
        been created.

        updated_at: date of the instance in which it has
        been updated.
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        change the representation of the instance
        and shows it's name, id, and dict.
        """
        return ("[{}] ({}) {}"
                .format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the updated_at attribute with the
        current date.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys and values
        of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
