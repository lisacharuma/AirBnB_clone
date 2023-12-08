#!/usr/bin/python3
from models.base_model import BaseModel
"""Review module"""


class Review(BaseModel):
    """represents Reviews"""
    place_id = ""
    user_id = ""
    text = ""
