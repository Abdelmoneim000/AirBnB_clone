#!/usr/bin/python3
"""
console Program that contains the entry
point of the command interpreter
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
    """defines each command"""
    prompt = "(hbnb) "

    dict_model = {
            'BaseModel': BaseModel,
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
    }

    def default(HBNBCommand, line):
        """default method to customise
           how thing should works
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
        '''exit the program'''
        return True

    def do_EOF(self, line):
        '''exit the program'''
        return True

    def do_create(self, line):
        ''' Creates a new instance of BaseModel '''
        if line == '':
            print('** class name missing **')
            return

        else:
            for cl, val in HBNBCommand.dict_model.items():
                if cl == line:
                    obj = val()
                    print(obj.id)
                    obj.save()
                    return
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of
            an instance based on the class name
        '''
        if line == '':
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
            '''storage.reload()'''
            obj = storage.all()
            j = 0
            ky = args[0] + '.' + args[1]
            if obj.get(ky) is None:
                print('** no instance found **')
            else:
                print(obj.get(ky))

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        if line == '':
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
                with open('file.json', 'w') as fh:
                    json.dump(dict1, fh)

    def do_all(self, line):
        ''' Prints all string representation of all
            instances based or not on the class name
        '''
        obj = storage.all()
        if line == '':
            lst = []
            for key, value in obj.items():
                lst.append(value.__str__())
            print(lst)

        else:
            if HBNBCommand.dict_model.get(line) is None:
                print("** class doesn't exist **")
                return
            lst = []
            for key, value in obj.items():
                if line in key:
                    lst.append(value.__str__())
            print(lst)

    def do_update(self, line):
        '''  Updates an instance based on the class name
             and id by adding or updating attribute
             (save the change into the JSON file).
        '''
        if line == '':
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
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            if args[2] == "id" or args[2] == "created_at"\
                    or args[2] == "updated_at":
                return
            var = obj[ky]
            '''set attribute'''
            attr = args[2]
            try:
                att_value = eval(args[3])
            except Exception:
                att_value = args[3]
            setattr(var, attr, att_value)
            var.save()

    def do_count(self, line):
        """count number of instance of specific class"""
        if line == "":
            print('** class name missing **')
            return False
        elif HBNBCommand.dict_model.get(line) is None:
            print("** class doesn't exist **")
            return False
        obj = storage.all()
        count = 0
        for key in obj.keys():
            if line in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
