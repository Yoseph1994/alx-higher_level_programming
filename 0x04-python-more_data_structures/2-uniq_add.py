#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    traversed = []
    sum = 0
    for el in my_list:
        if el not in traversed:
            sum += el
            traversed.append(el)
    return sum
