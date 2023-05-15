#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel



class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects.

        Only if the JSON file (__file_path) exists. Otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = key.split(".")[0]
                    self.__objects[key] = eval(class_name)(**value)
        except:
            pass
