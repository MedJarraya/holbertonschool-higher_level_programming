#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        new = (ln, None)
    else:
        new = (ln, sentence[0])
    return new
