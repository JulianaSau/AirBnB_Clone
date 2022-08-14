#!/ussr/bin/python3
'''Module for Review class'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Class representation of a Review'''

    place_id = ""  # will be Place.id
    user_id = ""  # will be User.id
    text = ""
