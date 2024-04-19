#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_i = []
    for k, v in a_dictionary.items():
        if v == value:
            del_i.append(k)
    for i in del_i:
        del a_dictionary[i]
    return a_dictionary
