#!/usr/bin/python3
import cmd
"""Console module"""


class HBNBCommand(cmd.Cmd):
    """Contains entry point to the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Does nothing on empty input line"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits program with Ctrl^D"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
