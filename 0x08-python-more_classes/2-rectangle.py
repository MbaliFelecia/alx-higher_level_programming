#!/usr/bin/python3
""" Module that creates an empty class of rectangle and defines it"""


class Rectangle:
    """ Empty class Rectanle"""

    def __init__(self, width=0, height=0):
        """ Method to initialze instances

        Args:
            width: the width of the rectangle instance
            height: the height of the rectangle instance
        Raises:
            TypeError: if width or height is not integers
            ValueError: if with or height is less than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Method that retrives the width

        Returns:
            width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Method that set the width

        Args:
            value: the value to be set
        Raises:
            TypeError: If width is not an interger
            ValueError: If width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @propety
    def height(self):
        """ Method that retrive the height

        Returns:
            the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Method to set the height

        Args:
            value: the value to be set
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Module that calculates the area of rectangle instance"""
        
        return self.__width * self.__height

    def perimeter(self):
        """ module that calculates the perimeter of rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))



