#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
"""Console module"""


class HBNBCommand(cmd.Cmd):
    """Contains entry point to the command interpreter"""
    prompt = "(hbnb) "
    class_names = ["BaseModel"]

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

    def do_create(self, line):
        """Creates a new BaseModel instance, saves and prints id
        create <class_name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints string rep of an instance based on class name
        show <class_name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            """Check objects in storage"""
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objs:
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, line):
        """Deletes an instance of a class
        destroy <class_name> <id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            """Check objects in storage"""
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objs:
                print("** no instance found **")
            else:
                del objs[key]
                storage.save()

    def do_all(self, line):
        """Prints str rep of all instances
        all <class_name>
        """
        args = line.split()
        obj_list = []
        objs = storage.all()
        if len(args) == 0:
            for key, value in objs.items():
                obj_list.append(str(value))
            print(obj_list)
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            for key, value in objs.items():
                if key.startswith(class_name):
                    obj_list.append(str(value))
            print(obj_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
