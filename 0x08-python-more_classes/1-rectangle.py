#!/usr/bin/python3
""" class module that create an empty class Rectangle and defines a rectangle"""


class Rectangle:
    """ Empty classs Rectangle"""

    def __init__(self, width=0, height=0):
        """ A method to initialize instances

        Args:
            width: the width of a rectangle instance
            height: the height of a rectangle instance
        Raises:
            TypeError: if the width or height is not integers
            ValueError: if the width or height is less than 0
        """


        self.width = width
        self.height = height

    @property
    def width(self):
        """ Method that retrieves the value of the width

        Returns:
        rectangle width
        """
        return self.__width

    @width.setter
    def width(self, Value):
        """ Method to set the width

        Args:
            Value: Value to be set
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that retrieves the value of the height

        Returns:
            rectangle height
        """

        return self.__height
        
    @height.setter
    def height(self, value):
        """ method to set the height

        Args:
            Value: Value to be set
        Raises:
            TypeError: If height is not integer
            ValueError: If height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            
        self.__height = value

        
