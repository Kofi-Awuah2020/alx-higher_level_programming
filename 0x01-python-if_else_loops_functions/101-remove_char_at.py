#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    else:
        newstring = list(str)
        del newstring[n]
        return ''.join(newstring) # Join methd concatenates the list into string
