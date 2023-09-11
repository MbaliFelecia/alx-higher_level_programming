#!/usr/bin/python3
""" Function that returns True/False if obj is an instance of a_class
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/Flase of obj is an instance of a_class

    Args:
        obj: oject
        a_class: class type

    Returns:
        True is obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
