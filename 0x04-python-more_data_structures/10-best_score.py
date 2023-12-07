#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        new_dict = max(a_dictionary, key=a_dictionary.get)
        return new_dict
