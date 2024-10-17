#!/usr/bin/python3

"""A module with a function that appends to a file"""


def append_write(filename="", text=""):
    """
    Writes to a file

    Args:
    filename(str): The name of the file to be written to
    text: text to be appended
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        length = file.write(text)
        return length
