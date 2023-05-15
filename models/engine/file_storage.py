#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


import json

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
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**obj_dict)
        except FileNotFoundError:
            pass
