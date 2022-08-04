#!/usr/bin/python3

"""
File storage engine
"""

import json
from datetime import datetime
from models.base_model import BaseModel

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
MODELS = [BaseModel]


class FileStorage:
    """
    class implementation of file storage
    """

    __file_path: str = 'file.json'
    __objects: dict = {}

    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def all(self):
        """
        :returns: the dict __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        :param obj: instance
        sets in __objects the obj with ket <obj classname>.id
        """
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to json (in __file_path)
        """
        # print(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, json_file)

        # because save() overwrites __dict__ as to_dict(), \
        # reconvert the datetime str to obj and \
        # remove __class__
        for k, v in FileStorage.__objects.items():
            obj_dict = v.__dict__
            for ck, cv in v.__dict__.items():
                if ck in ('created_at', 'updated_at'):
                    v.__dict__[ck] = datetime.strptime(cv, DATE_FORMAT)
            v.__dict__.__delitem__('__class__')

    def reload(self):
        """
        deserializes the json file to __objs
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as json_file:
                dict_objs = json.load(json_file)

            if dict_objs:
                for k, v in dict_objs.items():
                    class_name, obj_id = k.split('.')
                    for class_model in MODELS:
                        if class_model.__name__ == class_name:
                            obj = class_model(**v)
                            self.new(obj)

        except FileNotFoundError:
            pass
