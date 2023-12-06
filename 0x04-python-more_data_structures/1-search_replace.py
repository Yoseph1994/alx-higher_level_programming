#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        if search in my_list:
            idx = my_list.index(search)
            my_list[idx] = replace
            new_list = [*my_list]
            return new_list
