#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict_new = {}
    for key, val in a_dictionary.items():
        dict_new.update({key: (val * 2)})
    print(dict_new)
    return dict_new
