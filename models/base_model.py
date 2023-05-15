#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()



class BaseModel:
    """Base class for other classes"""

    def __init__(self, *args, **kwargs):
            """
    Initializes a new instance of BaseModel.
    If kwargs is not empty, sets instance attributes based on key/value pairs
    in kwargs. Otherwise, initializes new instance with unique id and created_at.
    """
    if kwargs:
        for k, v in kwargs.items():
            if k == "__class__":
                continue
            if k == "created_at" or k == "updated_at":
                v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, k, v)
    else:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
    """
    Updates the public instance attribute updated_at with the current
    datetime and saves the instance to the storage.
    """
    self.updated_at = datetime.now()
    storage.save()


    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
