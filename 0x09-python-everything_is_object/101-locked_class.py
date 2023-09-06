#!/usr/bin/python3
"""

module that contains a class that avoids
dynmically created attributes

"""


class LockedClass:
    """A class that only take 'first_name' attribute"""
    __slots__ = ['first_name']

    def __init__(self):
        """ A method to intialize"""
        pass
