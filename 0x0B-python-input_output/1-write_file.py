#!/usr/bin/python3

"""A module with a function that writes to file"""


def write_file(filename="", text=""):
    """
    Writes to file

    Args:
    filename(str): The name of the file to be written to
    text: text to be written to file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        length = file.write(text)
        return length
