#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary == dict():
        return None
    return sorted(list(a_dictionary.items()))[-1][0]
