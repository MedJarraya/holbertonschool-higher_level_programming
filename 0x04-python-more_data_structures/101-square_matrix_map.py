#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda k: list(map(lambda w: w*w, k)), matrix)))
