#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            obj_dict = {}
            for k, v in self.__objects.items():
                obj_dict[k] = v.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the JSON file exists).
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name, obj_id = k.split(".")
                    cls = globals()[class_name]
                    obj = cls(**v)
                    self.__objects[k] = obj
