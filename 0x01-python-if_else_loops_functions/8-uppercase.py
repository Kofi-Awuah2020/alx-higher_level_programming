#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            new_str += "{0:c}".format(ascii_value - 32)
        else:
            new_str += "{0:s}".format(char)
    print("{:s}".format(new_str))
