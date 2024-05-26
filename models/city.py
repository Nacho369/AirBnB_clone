#!/usr/bin/python3
"""Defines a City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City Class"""
    state_id = ""
    name = ""
