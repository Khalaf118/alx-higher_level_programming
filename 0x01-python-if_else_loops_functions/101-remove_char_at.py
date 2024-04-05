#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str_n = str[:n] + str[(n+1):]
    else:
        str_n = str
    return str_n
