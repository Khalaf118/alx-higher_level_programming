#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    index_list = []
    for i in range(len(string_list)):
        if string_list[i] == 'c' or string_list[i] == 'C':
            index_list.append(i)
    for i in index_list:
        del string_list[i]
    return ''.join(string_list)
