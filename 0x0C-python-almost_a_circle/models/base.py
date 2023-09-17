#!/usr/bin/python3
""" Module  with a class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Intializes instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted to JSON.

        Returns:
            str: The JSON string representation of the list_dictionaries.
        """
    if not list_dictionaries or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)
