#!/usr/bin/python3

"""
console
"""

# pylint:disable=broad-except, unused-argument, invalid-name


import cmd
import re

import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

MODELS = [BaseModel, User, State, City, Amenity, Place, Review]


class HBNBCommand(cmd.Cmd):
    """
    hbnb CLI implementation
    """

    prompt = '(hbnb) '

    ERROR_MSGS = {
        "no_class": "** class name missing **",
        "invalid_class": "** class doesn't exist **",
        "no_id": "** instance id missing **",
        "invalid_id": "** no instance found **",
        "too_many": "** too many arguments **",
        "no_attrib": "** attribute name missing **",
        "no_value": "** value missing **"
    }

    def str_to_class(self, model: str):
        """
        :return: class obj from str
        """
        class_obj = None
        try:
            if globals()[model]:
                class_obj = globals()[model]
        except Exception:
            pass
        return class_obj

    def do_quit(self, line):
        """
        quit console
        """
        return True

    def do_EOF(self, line):
        """
        quit console on EOF
        """
        return True

    def check_input(self, line):
        """
        checks if input exist
        """
        has_input = False
        if line == "":
            print(self.ERROR_MSGS['no_class'])
        else:
            has_input = True
        return has_input

    def handle_input(self, line: str, arg_len: int,
                     should_delete: bool = False):
        """
        handler for one input operations
        """
        has_input = self.check_input(line)
        # if line == "":
        #     print(self.ERROR_MSGS['no_class'])
        #     return
        # else:

        argv = line.split(" ")
        argc = len(argv)
        # too_many_args = False

        if arg_len == 1:
            # one input handling
            # usually model
            model_class = None  # avoid unpack error

            if has_input:
                if argc == 1:
                    model_class = self.str_to_class(argv[0])
                    # return model_class
                else:
                    print(self.ERROR_MSGS['too_many'])
            return model_class

        if arg_len == 2:
            # two inputs
            # model and id
            model_class = None
            instance = None

            if has_input:
                if argc == 2:
                    model_name, obj_id = argv
                    model_class, instance = models.\
                        storage.find(model_name, obj_id, should_delete)
                    # print(model_class, instance)

                    if model_class is None:
                        # if self.str_to_class()
                        print(self.ERROR_MSGS['invalid_class'])
                    elif instance is None:
                        print(self.ERROR_MSGS['invalid_id'])
                    # else:
                    #     # print(str(instance))
                    #     return model_class, instance

                elif argc == 1:
                    print(self.ERROR_MSGS['no_id'])

                else:
                    print(self.ERROR_MSGS['too_many'])
            return model_class, instance

        if arg_len == 4:
            # four inputs
            # model, id, attribute, value
            model_class = instance = attrib = value = None

            if has_input:
                if argc == 1:
                    print(self.ERROR_MSGS['no_id'])
                elif argc == 2:
                    print(self.ERROR_MSGS['no_attrib'])
                elif argc == 3:
                    print(self.ERROR_MSGS['no_value'])
                else:
                    model_name, obj_id, attrib, value = argv[:4]
                    model_class, instance = models.\
                        storage.find(model_name, obj_id, should_delete)
                    if model_class is None:
                        print(self.ERROR_MSGS['invalid_class'])
                    elif instance is None:
                        print(self.ERROR_MSGS['invalid_id'])
            return model_class, instance, attrib, value

        # else:
        print('** Accepted values are 1, 2 and 4 **')

    def do_create(self, line):
        """
        Creates an instance from the valid model argument
        """

        model_class = self.handle_input(line, 1)
        if model_class:
            obj = model_class()
            # models.storage.new(obj)
            obj.save()
            print(obj.id)
        else:
            print(self.ERROR_MSGS['invalid_class'])

    def do_show(self, line: str):
        """
        Show instance of model with specified id
        """
        model_class, instance = self.handle_input(line, 2)
        if instance:
            print(str(instance))

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        model_class, instance = self.handle_input(line, 2, True)
        # if instance:
        #     print(f"** {instance.id} destroyed **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        array = []
        model_class = None
        if line == "":
            for header, obj in models.storage.all().items():
                array.append(str(obj))
        else:
            model_class = self.handle_input(line, 1)
            if model_class:
                for header, obj in models.storage.all().items():
                    if header.split(".")[0] == model_class.__name__:
                        array.append(str(obj))
            elif (not model_class) and (len(line.split(" ")) == 1):
                print(self.ERROR_MSGS['invalid_class'])

        if array:
            print(array)
        else:
            if model_class:
                print(self.ERROR_MSGS["invalid_id"])

    def do_update(self, line):
        """
         Updates an instance based on the class name and id
         by adding or updating attribute
        """

        model_class, instance, attrib, value = self.handle_input(line, 4)
        if instance and attrib and value:
            str_pat = r"^\"[\S]+\"$"
            value_is_str = re.match(str_pat, value)
            adjusted_value = None

            if value_is_str:
                adjusted_value = value_is_str.group().replace("\"", "")
            else:
                try:
                    adjusted_value = int(value)
                except ValueError:
                    try:
                        adjusted_value = float(value)
                    except ValueError:
                        print("** Invalid value format for attribute **")

            if adjusted_value:
                setattr(instance, attrib, adjusted_value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
