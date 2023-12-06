#!/usr/bin/python3
def uniq_add(my_list=[]):
    traversed=[]
    sum=0
    for el in my_list:
        if el not in traversed:
            sum +=el
            traversed.append(el)
    return sum
