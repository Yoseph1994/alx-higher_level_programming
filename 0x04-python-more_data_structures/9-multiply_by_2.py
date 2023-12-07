#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiple = {}
    for i in a_dictionary:
        multiple[i] = a_dictionary[i] * 2
    return multiple
