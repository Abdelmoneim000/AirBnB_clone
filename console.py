#!/usr/bin/python3
"""
My cosnole program:
  start it by running the file (console.py)
  type help to see list of commands.
  type help <command> to see the command dict.
"""


from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import cmd
import os
import json


class HBNBCommand(cmd.Cmd):
    """
    Class to run the program using cmd
    module.
    Defines all commands.
    """
    prompt = "(hbnb) "

    dict_model = {
            'BaseModel': BaseModel,
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
    }

    def default(HBNBCommand, line):
        """
        First default method to customise
        the Program.
        """
        cmnd_dict = {
                "all": HBNBCommand.do_all,
                "show": HBNBCommand.do_show,
                "destroy": HBNBCommand.do_destroy,
                "count": HBNBCommand.do_count,
                "update": HBNBCommand.do_update
        }
        args = line.split(".")
        try:
            if len(args) != 2:
                print(f"*** Unknown syntax: {line}")
                return False
            if HBNBCommand.dict_model.get(args[0]) is None:
                print(f"** class doesn't exist **")
                return False
            commandss = args[1].split("(")
            if len(commandss) != 2:
                print(f"*** Unknown syntax: {line}")
                return False
            arg_line = args[0]
            if len(commandss[1]) > 1:
                commandss[1] = '(' + commandss[1]
                commandss[1] = commandss[1][:-1]
                commandss[1] = commandss[1] + ",)"
                commands_tuple = eval(commandss[1])
                if len(commands_tuple) > 1 and type(commands_tuple[1]) is dict:
                    arg_line += ' ' + commands_tuple[0]
                    for key, value in commands_tuple[1].items():
                        update_str = arg_line
                        update_str += " " + str(key) + " " + str(value)
                        for ky, vl in cmnd_dict.items():
                            if ky == commandss[0]:
                                vl(update_str)
                                break
                    return
                for i in commands_tuple:
                    arg_line += " " + i
            flag = 0
            for ky, vl in cmnd_dict.items():
                if ky == commandss[0]:
                    vl(arg_line)
                    flag = 1
                    break
            if flag == 0:
                print(f"*** Unknown syntax: {line}")
                return False
        except Exception:
            print(f"*** Unknown syntax: {line}")
            return False

    def do_quit(self, line):
        """Exit the program using quit command"""
        return True

    def do_EOF(self, line):
        """
        Exits the program using Ctrl+C or
        Ctrl+D
        """
        return True

    def do_create(self, line):
        """
        A command to create a new instance
        of BaseModel class
        """
        if line == '':
            print('** class name missing **')
            return

        else:
            for cls, val in HBNBCommand.dict_model.items():
                if cls == line:
                    objct = val()
                    print(objct.id)
                    objct.save()
                    return
            print("** class doesn't exist **")

    def do_show(self, line):
        '''
        Prints a string rep. of an instance.
        '''
        if line == "":
            print("** class name missing **")
            return
        arguments = line.split()

        if HBNBCommand.dict_model.get(arguments[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        else:
            """Reload storage"""
            objct = storage.all()
            j = 0
            ky = arguments[0] + '.' + arguments[1]
            if objct.get(ky) is None:
                print('** no instance found **')
            else:
                print(objct.get(ky))

    def do_destroy(self, line):
        """Deletes an instance Using ID and UserName"""
        if line == "":
            print('** class name missing **')
            return
        args = line.split()
        if HBNBCommand.dict_model.get(args[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            obj = storage.all()
            j = 0
            ky = args[0] + '.' + args[1]

            if obj.get(ky) is None:
                print('** no instance found **')
            else:
                del obj[ky]
                dict1 = {}
                for k, v in obj.items():
                    dict1[k] = v.to_dict()
                with open("file.json", "w") as f:
                    json.dump(dict1, f)

    def do_all(self, line):
        """
        Prints all str rep. of all instances.
        """
        obj = storage.all()
        if line == "":
            lst = []
            for key, value in obj.items():
                lst.append(value.__str__())
            print(lst)

        else:
            if HBNBCommand.dict_model.get(line) is None:
                print("** class doesn't exist **")
                return
            array = []
            for key, value in obj.items():
                if line in key:
                    array.append(value.__str__())
            print(array)

    def do_update(self, line):
        """
        Updates an instance Using className
        and id, adding or updatin attributes.
        (save the change into the JSON file).
        """
        if line == "":
            print('** class name missing **')
            return
        arguments = line.split()
        if HBNBCommand.dict_model.get(arguments[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print('** instance id missing **')
            return
        else:
            obj = storage.all()
            j = 0
            ky = arguments[0] + "." + arguments[1]
            if obj.get(ky) is None:
                print('** no instance found **')
                return
            if len(arguments) == 2:
                print("** attribute name missing **")
                return
            if len(arguments) == 3:
                print("** value missing **")
                return
            if arguments[2] == "id" or arguments[2] == "created_at"\
                    or arguments[2] == "updated_at":
                return
            variable = obj[ky]
            """set new attribute"""
            attr = arguments[2]
            try:
                att_value = eval(arguments[3])
            except Exception:
                att_value = arguments[3]
            setattr(variable, attr, att_value)
            variable.save()

    def do_count(self, line):
        """count number of instance of specific class"""
        if line == "":
            print('** class name missing **')
            return False
        elif HBNBCommand.dict_model.get(line) is None:
            print("** class doesn't exist **")
            return False
        objct = storage.all()
        count = 0
        for key in objct.keys():
            if line in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
