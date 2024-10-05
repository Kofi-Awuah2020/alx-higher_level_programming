#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        return max(tuple(a_dictionary.keys()))
    else:
        return None
