#!/usr/bin/python3
'''
This file contains the base model of all other classes
'''


from datetime import datetime
import uuid
from models import storage


class BaseModel:

    '''Class for base model of object heirarchy'''

    def __init__(self, *args, **kwargs):
        '''Initialises a base instance

            Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        '''
        if kwargs:
            kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_obj)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        Retuns the string representation of the class
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        Updates the public instance attribute updated_at with current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
            returns a dictionary containing all keys/values of __dict__ of the instance:
        '''

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
