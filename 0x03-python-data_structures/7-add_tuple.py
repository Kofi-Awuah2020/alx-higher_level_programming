#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_a = list(tuple_a)
    temp_b = list(tuple_b)

    if len(temp_a) == 1:
        temp_a.append(0)
    if len(temp_b) == 1:
        temp_b.append(0)
    if len(temp_a) == 0:
        temp_a = [0,0]
    if len(temp_b) == 0:
        temp_b = [0,0]
    
    add_temp = [0,0]
    add_temp = [temp_a[0] + temp_b[0], temp_a[1] + temp_b[1]]
    add_tuple = tuple(add_temp)
    return add_tuple
