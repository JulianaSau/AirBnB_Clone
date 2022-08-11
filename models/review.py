#!/usr/bin/python3
'''
Contains the Review Model
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A model for the Review
    Attributes:
        place_id (str): The id of the place being reviewed
        user_id (str): The id of the user who gave the review
        text (str): The actual review
    '''
    place_id = ""
    user_id = ""
    text = ""
