#!/usr/bin/bash
'''
Contains the base model for all other classes
'''

import models
import uuid
from datetime import datetime

class BaseModel:
    '''
    The base class for all other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initialises the base model
        '''
        if kwargs:
            kwargs.pop("__class__")
            for arg, value in kwargs.items():
                if arg == "created_at" or arg == "updated_at":
                    date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, arg, date_obj)
                else:
                    setattr(self, arg, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        def save(self):
            '''
            Updates the public instance attribute updated at
            with the current datetime
            '''
            self.updated_at = datetime.now()
            models.storage.save()

        def __str__(self):
            '''
            Returns a string representation of the object
            '''
            return ("[{}] ({}) {}".format(self.__class__.__name__
                , self.id, self.__dict__))

        def to_dict(self):
            '''
            Returns a dictionary containing a representation of the instance
            '''
            obj_dict = {}
            obj_dict['__class__'] = self.__class__.__name__
            for key, value in self.__dict__.items():
                if key == "created_at" or key == "updated_at":
                    date_str = value.isoformat()
                    obj_dict[key] = date_str
                else:
                    obj_dict[key] = value

            return obj_dict

