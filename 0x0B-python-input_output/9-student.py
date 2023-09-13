#!/usr/bin/python3
""" A class defination of student """


class Student:
    """ A class called Student """

    def__init__(self, first_name, last_name, age):
        """ A contractor method for the student class

        Args:
            first_name: the first name of a student instance
            last_name: the last_name of a student instance
            age: the age of a student instance
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A method that retrieves a dictinary representation of
            a student instance
        Returns:
            the dictionary representation of a sTudent instance
        """

        return self.__dict__
