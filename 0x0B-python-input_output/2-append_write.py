#!/usr/bin/python3
""" A module defining a fuction called append_write """


def append_write(filename="", text=""):
    """ A fuction that appends to a file

    Args:
        filename: the path to the file to be written on
        text: the string to be written
    Return:
        the number of characters written
    """

    with open(filename, "a", encoding="utf-8") as f:
        written = f.write(text)
        return (written)
