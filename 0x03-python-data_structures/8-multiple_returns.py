#!/usr/bin/python3
def multiple_returns(sentence):
    char = None
    size = len(sentence)
    if size > 0:
        char = sentence[0]
        return size, char
