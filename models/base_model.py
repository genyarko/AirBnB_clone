#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
from models import storage


import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in self.__dict__:
                self.__dict__["created_at"] = datetime.strptime(
                    self.created_at, "%Y-%m-%dT%H:%M:%S.%f"
                )
            if "updated_at" in self.__dict__:
                self.__dict__["updated_at"] = datetime.strptime(
                    self.updated_at, "%Y-%m-%dT%H:%M:%S.%f"
                )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
