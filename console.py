#!/usr/bin/python3

"""
console
"""

# pylint:disable=broad-except, unused-argument, invalid-name


import cmd
import models
from models.base_model import BaseModel

MODELS = [BaseModel]


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
        "too_many": "** too many arguments **"
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

    def do_create(self, line):
        """
        Creates an instance from the valid model argument
        """

        if line == "":
            print("** class name missing **")
        else:
            args = line.split(" ")
            model_class = self.str_to_class(args[0])
            if model_class is None:
                print("** class doesn't exist **")
            else:
                # print("** class name found **")
                obj = model_class()
                models.storage.new(obj)
                obj.save()
                print(obj.id)

    def do_show(self, line: str):
        """
        Show instance of model with specified id
        """
        if line == "":
            print(self.ERROR_MSGS['no_class'])

        else:
            argv = line.split()
            argc = len(argv)

            if argc == 2:
                model_name, obj_id = argv
                model_class, instance = models.storage.find(model_name, obj_id)
                # print(model_class, instance)

                if model_class is None:
                    print(self.ERROR_MSGS['invalid_class'])
                elif instance is None:
                    print(self.ERROR_MSGS['invalid_id'])
                else:
                    print(str(instance))

            elif argc == 1:
                print(self.ERROR_MSGS['no_id'])
            else:
                print(self.ERROR_MSGS['too_many'])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
