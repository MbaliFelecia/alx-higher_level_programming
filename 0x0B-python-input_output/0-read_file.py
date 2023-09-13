#!/usr/bin/python3
""" A module containing defination for the read_file function """


def read_file(filename=""):
    """ Afunction that reads data from a file

    Args:
        Filename: the name of the file to be read
    """

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
