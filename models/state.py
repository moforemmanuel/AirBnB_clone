#!/usr/bin/python3

"""
User Model
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class
    """

    name: str = ""
