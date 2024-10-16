#!/usr/bin/python3

"""A module with a function that reads from a file"""


def read_file(filename=""):
    """
    Reads a file from a file

    Args:
    filename(str): The name of the file to be read
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
