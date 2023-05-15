#!/usr/bin/python3
"""
Command interpreter for HBNB project
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit program with EOF (Ctrl-D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]

        if cls_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes[cls_name]()

        new_instance.save()

        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]

        if cls_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)

        if key not in storage.all().keys():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]

        if cls_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        inst_id = args[1]
        key = "{}.{}".format(cls_name, inst_id)

        if key not in storage.all().keys():
            print("** no instance found **")
            return

        storage.delete(key)
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        if not arg:
            print([str(val) for val in storage.all().values()])
            return

        args = arg.split()
        cls_name = args[0]

        if cls_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        print([str(val) for key, val in storage.all().items() if key.startswith(cls_name + '.')])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]

        if cls_name not in storage.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

