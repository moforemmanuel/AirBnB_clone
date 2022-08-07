#!/usr/bin/python3

"""
Review Model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
