#!/usr/bin/python3
'''
Contains the City Model
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    A model for the City
    Attributes:
        state_id (str): The id of the state the city is in
        name (str): The name of the City
    '''
    state_id = ""
    name = ""
