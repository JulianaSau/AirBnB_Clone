#!/usr/bin/python3
'''
Contains the file storage class
'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''
    The file storage class
    attributes:
        __file_path: A path to the json file
        __objects: A dictionary to store all objects
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Adds to __objects a new object
        '''
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        # serialize the dictionary
        json_dict = {}
        for k, obj in FileStorage.__objects.items():
            json_dict[k] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for k, v in json_dict.items():
                    self.all()[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            return
