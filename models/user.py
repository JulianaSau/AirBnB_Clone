#!/usr/bin/python3
'''
Module contains class user
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    A model for the user
    Attributes:
        email (str): The user's email
        password (str): The user's password
        first_name (str): The user's first name
        last_name (str): The user's last name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
