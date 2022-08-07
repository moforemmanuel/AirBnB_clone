#!/usr/bin/python3

"""
User Model
"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """
    User Class
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    # def __init__(self, *args, **kwargs):
    #     """
    #     constructor
    #     """
    #     super().__init__(*args, **kwargs)


if __name__ == "__main__":
    # from models import storage
    # from models.base_model import BaseModel
    # from models.user import User

    all_objs = models.storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new User --")
    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = User()
    my_user2.first_name = "John"
    my_user2.email = "airbnb2@mail.com"
    my_user2.password = "root"
    my_user2.save()
    print(my_user2)
