#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    list_result = []
    for i in range(list_len):
        if my_list[i] % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result
