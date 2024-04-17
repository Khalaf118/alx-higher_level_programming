#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_result = 0
    unique = set(my_list)
    for i in unique:
        sum_result += i
    return sum_result
