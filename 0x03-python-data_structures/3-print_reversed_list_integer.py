#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    my_rlist = my_list[:]
    my_rlist.reverse()
    for i in range(len(my_rlist)):
        print("{:d}".format(my_rlist[i]))
