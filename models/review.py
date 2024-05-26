#!/usr/bin/python3
"""Defines a Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review Class"""
    place_id = ""
    user_id = ""
    text = ""
