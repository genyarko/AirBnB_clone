#!/usr/bin/env python3
"""
This is the console.py module that provides a command line interface
for interacting with the HBNB data models.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter for the HBNB data models.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        This method is called when an empty line is entered in the console.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
