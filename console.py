#!/usr/bin/python3

"""
console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    hbnb CLI implementation
    """

    prompt = '(hbnb) '

    @staticmethod
    def do_quit(self):
        """
        quit console
        """
        return True

    @staticmethod
    def do_EOF(self):
        """
        quit console on EOF
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
