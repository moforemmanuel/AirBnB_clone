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
            if len(line.split(" ")) == 1:
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

    def my_count(self, class_n):
        """
        Method counts instances of a certain class
        """
        count_instance = 0
        for instance_object in models.storage.all().values():
            if instance_object.__class__.__name__ == class_n:
                count_instance += 1
        print(count_instance)

    def default(self, line):
        """Method to take care of following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation)
        Description:
            Creates a list representations of functional models
            Then use the functional methods to implement user
            commands, by validating all the input commands
        """
        names = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

        commands = {"all": self.do_all,
                    "count": self.my_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update}

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
            # print(args)

            if args[1] in ["all", "count"]:
                # print('args in it')
                commands[args[1]](args[0])
            elif args[1] in ["show", "destroy"]:
                commands[args[1]](args[0] + ' ' + args[2])
            elif args[1] == "update":
                params = re.match(r"\"(.+?)\", (.+)", args[2])
                if params.groups()[1][0] == '{':
                    dic_p = eval(params.groups()[1])
                    for k, v in dic_p.items():
                        commands[args[1]](args[0] + " " + params.groups()[0] +
                                          " " + k + " " + str(v))
                else:
                    rest = params.groups()[1].split(", ")
                    commands[args[1]](args[0] + " " + params.groups()[0] + " " +
                                      rest[0] + " " + rest[1])

        if not args or len(args) < 2 or args[0] not in names \
                or args[1] not in commands.keys():
            super().default(line)
        return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
