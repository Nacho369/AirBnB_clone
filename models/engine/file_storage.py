#!/usr/bin/python3
"""Defines a FileStorage Class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents a FileStorage class that serializes instances
    to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __object"""
        return (self.__objects)

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        That is create a dictionary and set key and value as
        `<obj class name>.id: obj`
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)

        obj_dict is an empty dictionary that would store the dictionary
        representation of __object value which is an instance of a class
        """
        obj_dict = {}

        for key, val in self.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as to_file:
            json.dump(obj_dict, to_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)

        In essence, this function creates a BaseModel Instance from
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as from_file:
                file_obj_dict = json.load(from_file)
            for key, val in file_obj_dict.items():
                obj = eval(val['__class__'])(**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
