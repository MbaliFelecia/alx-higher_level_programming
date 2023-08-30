#!/usr/bin/python3
"""Defination of class 'Square' with private instance attribute - size"""


class Square:
    """ Class Square that defines a square object
    """
    def __init__(self, size):
        """Initialize method that store the size of the square

        Args:
            param1 (int): size of the square
        """
        self.__size = size
