#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    s = [[element ** 2 for element in matrix[i]] for i in range(len(matrix))]
    return s
