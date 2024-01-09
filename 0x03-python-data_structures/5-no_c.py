#!/usr/bin/python3
def no_c(my_string):
    string_cpy = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        string_cpy += char
    return string_cpy
