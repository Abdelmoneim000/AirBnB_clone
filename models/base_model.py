"""
A model to define all base attributes and methods
"""

import uuid
import datetime
from models import storage

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
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == '__class__':
                    continue
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all keys and values
        of __dict__
        """
        init_Dict = {}
        init_Dict.update(self.__dict__)
        init_Dict.update({'__class__': type(self).__name__})
        init_Dict['created_at'] = self.created_at.isoformat()
        init_Dict['updated_at'] = self.updated_at.isoformat()
        return init_Dict
