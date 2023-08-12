#!/usr/bin/python3
"""console of airbnb project"""

import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Project Console: class file"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        """pass on empty line"""
        pass

    def help_quit(self):
        """Display quite help text"""
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
