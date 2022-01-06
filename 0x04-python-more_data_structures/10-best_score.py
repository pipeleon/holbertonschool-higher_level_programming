#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    if a_dictionary == None:
        return None
    for i, j in a_dictionary.items():
        if temp < j:
            best = i
        temp = j
    return best
