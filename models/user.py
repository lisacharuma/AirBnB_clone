#!/usr/bin/python3
from models.base_model import BaseModel
""" User module"""


class User(BaseModel):
    """Handles user details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
