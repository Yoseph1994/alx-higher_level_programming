#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return[[element ** 2 for element in submatrix] for submatrix in matrix]
