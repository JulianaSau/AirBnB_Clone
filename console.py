#!/usr/bin/python3
"""
Contains comand line interpreter
"""
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage
import cmd
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
    HBNBCommand - class containing functions and attributes of the console
    Attributes:
             prompt - The string to be displayed as the prompt
             __classes - Contains a dictionary of all classes
             __types - contains a dictionary of attributes and their values
                      to be abe to parse rge during the update method
    Methods:
            do_quit() - implements quit command
            do_EOF() - Takes care of EOF in the command buffer
            emptyline - Method called when an empty line is entered in
                       response to the prompt.
                       If this method is not overridden,
                       it repeats the last nonempty command entered.

    '''
    prompt = "(hbnb) "
    __classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    # This is a dictionary of attributes and their values so that we can
    # properly parse them during the update method
    __types = {
                "number_rooms": int, "number_bathrooms": int,
                "max_guest": int, "price_by_night": int,
                "latitude": float, "longitude": float
            }

    def do_quit(self, args):
        '''
        Implements quit command
        Args:
            args - string containing arguments
        '''
        raise SystemExit

    def do_EOF(self, args):
        '''
        do_EOF() - Takes care of EOF in the command buffer
        Args:
           args - stream from the standard input
        '''
        return True
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        '''
         emptyline - Method called when an empty line is entered in
                       response to the prompt.
                    If this method is not overridden,
                    it repeats the last nonempty command entered.
        '''
        pass

    def do_create(self, arg):
        '''
        do_create - Creates a new instance of BaseModel and
        saves it to Json file and prints the id
        '''
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            model_1 = HBNBCommand.__classes[arg]()
            model_1.save()
            print(model_1.id)

    def do_show(self, arg):
        '''
        do__show - prints the string rep of an instance\
        based on the class name and the id
        '''
        args = arg.split()
        '''
        Check if the class name has\
        been passed and whether it exists
        '''
        try:
            obj = args[0]
            if obj not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return

        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = obj + "." + str(id)
        new_dict = storage.all()

        try:
            print(new_dict[key])
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''
        do_destroy - Destroys an Object based on the class name and id
        '''
        args = arg.split()
        # Check if the class name has been passed and whether it exists
        try:
            obj = args[0]
            if obj not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except:
            print("** instance id missing **")
            return

        key = obj + "." + str(id)
        stored_objs = storage.all()

        try:
            del(stored_objs[key])
            storage.save()
        except Exception as e:
            print("** no instance found **")

    def do_all(self, arg):
        '''
        Prints all string representation of all instances based or not on
        the class name.
        '''
        obj_dict = storage.all()
        obj_list = []
        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            if arg not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                for k, obj in obj_dict.items():
                    if arg in k:
                        obj_list.append(str(obj))
                print(obj_list)

    def do_update(self, arg):
        '''
        updates an instnace based on the class na,e and id by adding
        or updating attribute(saving the chanege into JSON file
        '''
        args = arg.split()
        try:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except:
            print("** class name missing **")
            return

        try:
            id = args[1]
            key = class_name + "." + str(id)
            if key not in storage.all():
                print("** no instance found **")
                return
        except:
            print("** instance id missing **")
            return

        try:
            attribute = args[2]
        except:
            print("** attribute name missing **")
            return

        try:
            value = args[3]
        except:
            print("** value missing **")
            return

        # Properly parse the value
        if "\"" in value:
            value = value[1:-1]
        else:
            value = HBNBCommand.__types[attribute](value)

        obj = storage.all()[key]
        setattr(obj, attribute, value)
        obj.save()

        # Help functions
        def help_create(self):
            '''
            Help for the create method
            '''
            print("Creates a new instance of BaseModel,"
                  "saves it (to the JSON file)and prints the id. Ex:"
                  "$ create BaseModel")

        def help_show(self):
            '''
            Help for the show method
            '''
            print("show -  Prints the string representation of an instance\
            based on the class name and id.\
            Ex: $ show BaseModel 1234-1234-1234.")

        def help_destroy(self):
            '''
            Help for the destroy
            '''
            print("destroy - Deletes an instance based on the class name and id\
            (save the change into the JSON file).\
            Ex: $ destroy BaseModel 1234-1234-1234.\
    help_EOF = help_quit")

        def help_all(self):
            '''
            Help for the all method
            '''
            print("all - Prints all string representation of all instances\
            based or not on the class name. Ex: $ all BaseModel or $ all.")

        def help_update(self):
            '''
            Help for the update method
            '''
            print(" Updates an instance based on the class name and id\
            by adding or updating attribute\
            (save the change into the JSON file).\
            Ex: $ update BaseModel 1234-1234-1234\
            email 'aibnb@holbertonschool.com'.")

        def help_quit(self):
            '''
            Implements help for quit method
            '''
            print("Quit command to exit the program")
            print()

        def help_EOF(self):
            '''
            Implements help for quit method
            '''
            print("Quit command to exit the program")
            print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
