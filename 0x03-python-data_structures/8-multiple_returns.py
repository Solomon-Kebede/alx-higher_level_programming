#!/usr/bin/python3

def multiple_returns(sentence):
    len_str = len(sentence)
    if len_str == 0:
        return (0, None)
    elif len_str > 0:
        return (len_str, sentence[0])
