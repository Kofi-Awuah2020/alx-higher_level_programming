#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_value = 0
    max_key = None

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
