#!/usr/bin/python3

"""
BaseModel module
"""

from uuid import uuid4
from datetime import datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Class BaseModel
    """
    # __dict__ = {}

    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_obj = self.__dict__
        for k, v in dict_obj.items():
            if k in ("created_at", "updated_at"):
                dict_obj[k] = v.isoformat()

        dict_obj['__class__'] = type(self).__name__
        return dict_obj


if __name__ == "__main__":
    b = BaseModel()
    # print(b.id)
    # print(b.created_at)
    b.name = 'yo'
    print(b.to_dict())
    print(type(b.id))
