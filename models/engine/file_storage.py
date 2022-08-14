#!/usr/bin/python3
'''
Serialises instances to a JSON file and 
deserialises JSON files to instances

'''

import json
from datetime import datetime
import os


class FileStorage:
    '''
    Class that stores instances of BaseModel

        Atrributes:
        - __file_path: path to JSON file
        - __objects:  dictionary that will store all objects by 
        <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)

    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Adds a new object to __objects
        sets in __objects the obj with key <obj class name>.id
        '''
        # TODO: should these be more precise specifiers?
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''

        # serialize the dictionary
        json_dict = {}
        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(json_dict))

    def classes(self):
        '''
        Returns a dictionary of valid classes and their references
        '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        '''
        Deserializes JSON file into __objects
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            json_dict = json.load(file)
            json_dict = {key: self.classes()[value["__class__"]](**value)
                         for key, value in json_dict.items()
                         }
            # TODO: should this overwrite or insert?
            FileStorage.__objects = json_dict

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime,
                      "updated_at": datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
