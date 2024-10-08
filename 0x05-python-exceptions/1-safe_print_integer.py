#!/usr/bin/python3
def safe_print_integer(value):
    flag = ""
    try:
        print("{:d}".format(value))
        flag = True
    except (TypeError, ValueError):
        flag = False
    return flag
