#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    '''
    Inherits from BaseModel

        attributes:
        - email -  email address of user
        - password - password for user account
        - first_name - user's firstname
        - last_name - user's last name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
