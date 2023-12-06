#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    unique_list = set(my_list)
    sum = 0
    for el in unique_list:
        sum = sum + el
    return sum
