#!/usr/bin/python3
def matrix_divided(matrix, div):
    if matrix == [] or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/\
floats")
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for i in matrix:
        first_i = len(matrix[0])
        fol_i = len(i)
        if fol_i is not first_i:
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        new_matrix.append([round(j / div, 2) for j in i])
    return new_matrix
