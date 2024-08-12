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

from typing import List


def valid_entries_checker(matrix: List[List[int]]) -> bool:
    """
    This function checks if all the entires of the matrix are valid numerical type entires, this code can tolerate
    integer, floating point and complex values. It also checks that all the rows of the matrix are of list or tuple
    type only.

    Argument : A matrix

    Return Value: True if entries are valid, False otherwise

    """
    column_length = len(matrix[0])
    row_length = len(matrix)
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            return False

    for i in range(row_length):
        for j in range(column_length):
            if not isinstance(matrix[i][j], (int, float, complex)):
                return False

    return True


def valid_dimension_checker(matrix: List[List[int]]) -> bool:
    """
    This function checks if the dimensions of the given matrix are consistent, it also checks if the input is a list of
    empty lists.

    Argument: A matrix

    Return Value: True if dimentions are consistant, False otherwise

    """
    column_length = len(matrix[0])
    for row in matrix:
        if len(row) != column_length or len(row) == 0:
            return False

    return True


def matrix_multiply(
    matrix1: List[List[int]], matrix2: List[List[int]]
) -> List[List[int]]:
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


"""
If you have reached here, thanks for going through the code, I have come up with some possible edgecases which
you may wanna use. These can just be directly appended to the test-matmul.py file and can be run.

Test 1:

 def test_list_of_empty_matrix(self):    
        matrix1 = [[], []]
        matrix2 = [[1, 0], [0, 1]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)
Test 2: 

    def test_float_values(self):
        matrix1 = [[1.5, 2.5], [3.5, 4.5]]
        matrix2 = [[5.5, 6.5], [7.5, 8.5]]
        expected_result = [[27.0, 31.0], [53.0, 61.0]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

Test 3:

    def test_complex(self):
        matrix1=[[1j]]
        matrix2=[[1j]]
        expected_result=[[-1]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result) 

Test 4:

    def test_3D(self):
        matrix1 = [[-1, -2], [-3, -4]]
        matrix2 = [[[1,2,3], 6], [7, 8]]
        expected_result = [[-19, -22], [-43, -50]]
        with self.assertRaises(TypeError):
            matrix_multiply(matrix1, matrix2)

Test 5:

    def test_invalidmatrix(self):
        matrix1 = [-1,-2,-3,-4]
        matrix2 = [[[1,2,3], 6], [7, 8]]
        expected_result = [[-19, -22], [-43, -50]]
        with self.assertRaises(TypeError):
            matrix_multiply(matrix1, matrix2)

"""
