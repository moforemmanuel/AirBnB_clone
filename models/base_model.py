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
        self.id = str(uuid4())
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
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
