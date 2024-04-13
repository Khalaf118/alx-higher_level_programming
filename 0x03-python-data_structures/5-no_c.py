#!/usr/bin/python3
def no_c(my_string):
    string_list = [ch for ch in my_string if ch != 'c' and ch != 'C']
    return "".join(string_list)
