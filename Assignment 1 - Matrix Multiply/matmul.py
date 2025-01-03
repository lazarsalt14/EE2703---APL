"""
----------------------------------------------------------------------------------------------------------------------------------
Name: Nishanth Senthil Kumar
Roll No: EE23B049
Date: 8th August 2024
Description: Function to multiply two matrices.
Input: 2 matrices as arguments to the matrix_multiply function.
Output: The function matrix_multiply returns a list of lists (a matrix) that is the product of
the given two matrices.
Added Description: If the dimension of matrix one is n*m and other one is m*k, then the worst case time complexity of 
this code is O(n*m*k). The code contains 2 additional functions to check the consistancy of the dimensions of the matrix,
and a function to check if all the entries to the matrix are valid numerical types. These functions have been declared to avoid
repetition of code. 
The code has been formatted using the "Black" formatter upon completion to ensure compatibility on all systems. 
----------------------------------------------------------------------------------------------------------------------------------
"""

from typing import List, Union, Tuple

# creating an alias for the different possible data types a matrix may compose of using the typing module
Matrix = Union[
    List[List[Union[int, float, complex]]],
    List[Tuple[Union[int, float, complex]]],
    Tuple[List[Union[int, float, complex]]],
    Tuple[Tuple[Union[int, float, complex]]],
]


def valid_entries_checker(matrix: Matrix) -> bool:
    """
    This function checks if all the entires of the matrix are valid numerical type entires, this code can tolerate
    integer, floating point and complex values. It also checks that all the rows and columns of the matrix are of list or tuple
    type only.

    Argument : A matrix

    Return Value: True if entries are valid, False otherwise

    """
    column_length = len(matrix[0])
    row_length = len(matrix)

    if not isinstance(matrix, (list, tuple)):
        return False

    for row in matrix:
        if not isinstance(row, (list, tuple)):
            return False

    for i in range(row_length):
        for j in range(column_length):
            if not isinstance(matrix[i][j], (int, float, complex)):
                return False

    return True


def valid_dimension_checker(matrix: Matrix) -> bool:
    """
    This function checks if the dimensions of the given matrix are consistent, it also checks if the input is a list of
    empty lists, which is an invalid input.

    Argument: A matrix

    Return Value: True if dimentions are consistant, False otherwise

    """
    column_length = len(matrix[0])
    for row in matrix:
        if len(row) != column_length or len(row) == 0:
            return False

    return True


def matrix_multiply(
    matrix1: Matrix, matrix2: Matrix
) -> List[List[Union[int, float, complex]]]:
    """
    This function multiplies two matrices and returns the product matrix.
    This code also checks for certain basic errors in the inputs, checks to make sure that the matrices are of
    valid dimensions, that they are non-empty, and that they have all numerical inputs and raises errors if
    these conditions are not met. The code can handle float type entires as entires to the matrix elements.

    Arguments : Two matrices, matrix1 and matrix2

    Return Value: A matrix that is the product of the two given matrices

    """

    # checks if the input matrices are non empty, raises a ValueError if they are
    if not matrix1 or not matrix2:
        raise ValueError("Input matrices should not be empty.")

    # calling a function to check if the dimensions of the matrix is valid
    if not valid_dimension_checker(matrix1):
        raise ValueError("Matrix 1 is of invalid dimensions")

    if not valid_dimension_checker(matrix2):
        raise ValueError("Matrix 2 is of invalid dimensions")

    # row1 is the number of rows and column1 is the number of columns in matrix1
    column1_length = len(matrix1[0])
    row1_length = len(matrix1)

    # row2 is the number of rows and column2 is the number of columns in matrix2
    column2_length = len(matrix2[0])
    row2_length = len(matrix2)

    # checks if the matrix multiplication is defined for given matrices
    if column1_length != row2_length:
        raise ValueError(
            "Matrix Multiplication is not defined for given dimensions of matrices"
        )

    # Calls a function which checks if all entires of a matrix is a numerical value
    if not valid_entries_checker(matrix1):
        raise TypeError("Matrices has a non-numeric element")

    if not valid_entries_checker(matrix2):
        raise TypeError("Matrices has a non-numeric element")

    # Declaring the product matrix filled with zeros using list comprehension, which is faster than appending row after row
    product_matrix = [[0 for _ in range(column2_length)] for _ in range(row1_length)]

    # Computing the product, the row_sum variable sums up a row column pair, which becomes an element of the product matrix
    for i in range(row1_length):
        for j in range(column2_length):
            row_sum = 0
            for k in range(column1_length):
                row_sum += matrix1[i][k] * matrix2[k][j]
            product_matrix[i][j] = row_sum

    # returning the product matrix
    return product_matrix
