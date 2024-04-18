#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    keys = list(a_dictionary)
    best = keys[0]
    for k in keys:
        if a_dictionary[k] > a_dictionary[best]:
            best = k
    return best
