#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os
from collections import defaultdict
from typing import Dict, List, Type

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path: str = "file.json"
    __objects: Dict[str, BaseModel] = defaultdict()

    @staticmethod
    def all() -> Dict[str, BaseModel]:
        return FileStorage.__objects

    @staticmethod
    def new(obj: BaseModel) -> None:
        key: str = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    @staticmethod
    def save() -> None:
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d: Dict[str, dict] = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    @staticmethod
    def classes() -> Dict[str, Type[BaseModel]]:
        classes: Dict[str, Type[BaseModel]] = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    @staticmethod
    def reload() -> None:
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict: Dict[str, dict] = json.load(f)
            obj_dict = {k: FileStorage.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items
