#!/usr/bin/python3
def multiple_returns(sentence):
    new = []
    new.append(len(sentence))
    if len(sentence) == 0:
        new.append("None")
    else:
        new.append(sentence[0])
    return tuple(new)
