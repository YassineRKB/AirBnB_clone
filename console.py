#!/usr/bin/python3
"""console of airbnb project"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Project Console: class file"""
    prompt = "(hbnb)"
    classes = {"BaseModel"}

    def do_EOF(self, line):
        """exits on eof detection"""
        print()
        return True

    def do_quite(self, line):
        """exit on eof detection"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
