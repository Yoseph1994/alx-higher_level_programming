#!/usr/bin/python3
def no_c(my_string):
    my_string=my_string.lower()
    my_string=[char for char in my_string]
    while 'c' in my_string:
        my_string.remove('c')
        new_string=''.join(my_string)
        return new_string
