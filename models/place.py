#!/usr/bin/python3
'''
Contains the Place Model
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    A model for the Place
    Attributes:
        city_id (str): The id of the city the place is in
        user_id (str): The id of the user who owns the place
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms the place has
        number_bathrooms (int): The number of bathrooms the place has
        max_guest (int): The maximum number of guests the place can hold
        price_by_night (int): The price per night of stay
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list of strings): A list of amenity ids
    '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
