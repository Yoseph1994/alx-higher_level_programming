#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        new_list=[replace if el==search else el for el in my_list ]
        return new_list
