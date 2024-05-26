#!/usr/bin/python3
"""Defines a HBNBCommand Class"""

import cmd
from shlex import split
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(arg):
    """Defines the function to parse argument passed"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Represent a HBNBCommand Class"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review}

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(args[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, line):
        """Quit command to exit the program"""
        return (True)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return (True)

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        Create an instance of a BaseModel, saves it (to the JSON file)
        and prints the id

        Ex: $ create BaseModel
        """
        args = split(arg)

        if len(arg) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            new_model = self.classes[arg]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id

        Ex: $ show BaseModel 1234-1234-1234
        """
        args = split(arg)
        obj_dict = storage.all()

        if len(arg) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file).

         Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = split(arg)
        obj_dict = storage.all()

        if len(arg) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
            if key in obj_dict:
                obj_dict.pop(key)
                storage.save()
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.

        Ex: $ all BaseModel or $ all.
        """
        # args = arg.split()
        # obj_dict = storage.all()

        # if len(arg) == 0:
        #     print([str(val) for val in obj_dict.values()])
        # elif arg not in self.classes.keys():
        #     print("** class doesn't exist **")
        # else:
        #     print([str(val) for key, val in obj_dict.items() if arg in key])

        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = split(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]

            if key in obj_dict:
                setattr(obj_dict[key], args[2], args[3])
                obj_dict[key].save()
            else:
                print("** no instance found **")
    
  
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
