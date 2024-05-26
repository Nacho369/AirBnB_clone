#!/usr/bin/python3
"""Defines a User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
