#!/usr/bin/python3
"""console of airbnb project"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Project Console: class file"""
    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def do_show(self, line):
        """shows string representaion of an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_name = f"{class_name}.{args[1]}"
        if instance_name not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[instance_name])

    def do_create(self, line):
        """Creates a new instance and saves it to storage"""
        if not line:
            print("** class name missing **")
            return
        class_name = line.strip()
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance = eval(line)()
        instance.save()
        print(instance.id)

    def do_destroy(self, line):
        """Destroys an instance using class name and instance id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        instance_name = f"{class_name}.{instance_id}"
        if instance_name not in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[instance_name]
            storage.save()

    def do_all(self, line):
        """Shows string representation of all instances"""
        args = line.split()
        objects = []
        if not args:
            objects = list(storage.all().values())
        elif args[0] in HBNBCommand.classes:
            class_name = args[0]
            for key, obj in storage.all().items():
                if class_name in key:
                    objects.append(obj)
        else:
            print("** class doesn't exist **")
            return
        print(objects)

    def do_update(self, line):
        """Updates instance attributes using class name and id"""
        args = line.split()
        if len(args) >= 4:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            new_value = " ".join(args[3:]).strip('"').strip("'")
            key = f"{class_name}.{instance_id}"
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            instance = storage.all()[key]
            if not hasattr(instance, attribute_name):
                print("** attribute doesn't exist **")
                return
            setattr(
                instance,
                attribute_name,
                type(getattr(instance, attribute_name))(new_value)
            )
            storage.save()
        else:
            print("** incorrect number of arguments **")

    def emptyline(self):
        """pass on empty line"""
        pass

    def help_quit(self):
        """Display quite help text"""
        print("Quit command to exit the program\n")

    def help_show(self):
        """Display quite help text"""
        print("show command to show instance of the class\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
