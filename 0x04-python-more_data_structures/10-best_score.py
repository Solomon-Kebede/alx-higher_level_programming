#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if a_dictionary == {}:
            return None
        else:
            return sorted(list(a_dictionary.items()))[-1][0]
    else:
        return None
