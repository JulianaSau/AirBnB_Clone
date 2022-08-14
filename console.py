#!/usr/bin/python3
'''Module for the Entry point of the command interpreter'''

import cmd
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    Class for the command interpreter
    '''
    prompt = "(hbnb) "
    intro = "Welcome to hbnb console! Type ? to list commands"

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            print("\"{}\" is not a recognised command".format(line))
            return print()
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_quit(self, input):
        '''
        Quit command to exit the program
        '''
        print("Bye")
        return True

    def do_EOF(self, input):
        '''
        Handles end of file character(ctrl + D)
        Quit command to exit the program
        '''
        print()
        return True

    def emptyline(self):
        '''
        Method called when an empty line is entered in response to the prompt.
        If this method is not overridden, it repeats the last nonempty command entered.
        '''
        pass

    def do_create(self, input):
        '''
        Creates an instance of BaseModel, saves it to JSON file
        and returns the id
        Ex: $ create BaseModel
        '''
        if input == "" or input is None:
            print("** class name missing **")
        elif input not in storage.classes():
            print("** class doesn't exist **")
        else:
            # create the instance
            new_instance = storage.classes()[input]()
            new_instance.save()
            print(new_instance)

    def do_show(self, input):
        '''
         Prints the string representation of an instance based 
         on the class name and id. 
         Ex: $ show BaseModel 1234-1234-1234.
        '''

        args = input.split()

        if input == "" or input is None:
            print("** class name missing **")
        else:
            if args[0] not in storage.classes():
                print("** class doesnt exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # instance id
                instance_id = "{}.{}".format(args[0], args[1])
                if instance_id not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[instance_id])

    def do_destroy(self, input):
        '''
         Deletes an instance based on the class name and 
         id (save the change into the JSON file). 
         Ex: $ destroy BaseModel 1234-1234-1234.
        '''

        args = input.split()

        if input == "" or input is None:
            print("** class name missing **")
        else:
            if args[0] not in storage.classes():
                print("** class doesnt exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                # instance id
                instance_id = "{}.{}".format(args[0], args[1])
                if instance_id not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[instance_id]
                    storage.save()

    def do_all(self, input):
        '''
        Prints all string representation of all instances 
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        '''

        obj_dict = storage.all()
        obj_list = []
        if not input:
            # appending all objects in storage to obj_list
            for object in obj_dict.values():
                obj_list.append(str(object))
            print(obj_list)
        else:
            if input not in storage.classes():
                print("** class doesn't exist **")
            else:
                for key, object in obj_dict.items():
                    if input in key:
                        obj_list.append(str(object))
                print(obj_list)

    def do_update(self, input):
        '''
        Updates an instance based on the class name and id by 
        adding or updating attribute (save the change into the JSON file). 
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        '''

        if input == "" or input is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, input)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            # check if class exists in storage
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                # casting the values
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                # setting value of the attribute
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, input):
        '''
        Retrieves the number of instances of a class: 
        Ex: $ <class name>.count().
        '''

        args = input.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                key for key in storage.all() if key.startswith(
                    args[0] + '.'
                )
            ]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
