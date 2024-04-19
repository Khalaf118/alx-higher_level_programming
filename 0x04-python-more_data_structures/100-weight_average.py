#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    num, denom = 0, 0
    for x in my_list:
        num += x[0] * x[1]
        denom += x[1]
    return (num/denom)
