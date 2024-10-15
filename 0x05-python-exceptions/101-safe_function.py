#!/usr/bin/python
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
