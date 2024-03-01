#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence.strip()) == 0:
        newt = 0, None,
        return newt
    else:
        newt = len(sentence), sentence.strip()[0],
        return newt
