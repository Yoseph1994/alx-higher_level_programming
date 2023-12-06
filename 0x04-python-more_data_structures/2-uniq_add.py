#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list=set(my_list)
    sum=0
    for unique_el in unique_list:
        sum=sum+unique_el
    return sum
