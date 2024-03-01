#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    owner = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > score:
            score = a_dictionary[key]
            owner = key
    return owner
