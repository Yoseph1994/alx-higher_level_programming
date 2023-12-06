#!/usr/bin/python3
def square_matrix_map(matrix=[]):
"""
Returns a new matrix with squared values of all integers in the input matrix,
without modifying the original matrix.

Args:
matrix: A list of lists representing the 2D matrix.

Returns:
A new list of lists containing squared values of the original matrix.
"""

def square_row(row):
return list(map(lambda x: x\*\*2, row))

return list(map(square_row, matrix))