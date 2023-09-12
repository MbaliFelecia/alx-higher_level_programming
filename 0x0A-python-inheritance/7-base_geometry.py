#!/usr/bin/python3
""" Class that defines the attributes of Geometric Shapes """


class BaseGeometry:
    """ Class that defines the attributes of Geometric Shape """

    def area(self):
        """ Method that defines the area of a geomtric shape
        Raises:
            Exception: Always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Args:
            name: name of the object
            value: value of the property
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an interger".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
