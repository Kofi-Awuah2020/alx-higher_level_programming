#!/usr/bin/python3
def multiple_returns(sentence):
    result = ()
    if len(sentence) == 0:
        result = (0, None)
        return result
    result = (len(sentence), sentence[0])
    return result
