#!/usr/bin/python3
""" class module creates an empty class and defines a rectangle"""


class Rectangle:
    """ Empty classs Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Method that retrieves the value of the width

        Returns:
        rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
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

    def area(self):
        """ Module that calculates the area of rectangle instance

        Returns:
            rectangle area

        """

        return self.__width * self.__height

    def perimeter(self):
        """ module that calculates the perimeter of rectangle instance

        Returns:
            rectangle perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Module that formats the output of print() and str()

        Returns:
            empty string if width or height is 0 otherwise rectangle shape
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method to format the outpt of repr() function

        Returns:
            the string representation of an object
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance id deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
~                                                     
