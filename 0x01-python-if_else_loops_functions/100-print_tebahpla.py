#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2 == 0:
        print("{0:c}".format(char), end='')
    else:
        print("{0:c}".format(char).upper(), end='')
