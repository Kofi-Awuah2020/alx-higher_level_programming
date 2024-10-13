#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    flag = ""
    try:
        print("{:d}".format(value))
        flag = True
    except (TypeError, ValueError) as ex:
        print("Exception:", ex,  file=sys.stderr)
        flag = False

    return flag
