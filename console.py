#!/usr/bin/python3
"""
A module to run the CLI as
an entry point.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Initiates the class for Cmd module
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles end of file EOF"""
        return True

    def do_quit(self, *args):
        """
        Quits the programm when typing quit
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
