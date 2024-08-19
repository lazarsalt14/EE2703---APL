def matrix_multiply(A, B):
    """
    Name: Arjun Kswamy
    RollNo : EE23B009
    Input : Two matrices ( A : (m,n))
    Output : Product matrix
    """

    check_empty_matrix(A, B)
    check_row_size(A, B)
    check_incompatible_dimension(A, B)
    check_non_numeric_values(A, B)

    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Initalising output matrix of appropriate dimensions consisting of only zeros
    out = [[0 for i in range(p)] for j in range(m)]

    # Performing matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                out[i][j] += A[i][k] * B[k][j]
    return out

    # Placeholder implementation that always raises NotImplementedError
    raise NotImplementedError("Matrix multiplication function not implemented")


def check_empty_matrix(A, B):
    # Checks for empty matrix
    if len(A) == 0 or len(B) == 0:
        raise ValueError()


def check_row_size(A, B):
    # checks if all rows have same length
    for i in range(len(A)):
        if len(A[0]) != len(A[i]):
            raise ValueError
    for i in range(len(A)):
        if len(A[0]) != len(A[i]):
            raise ValueError


def check_incompatible_dimension(A, B):
    # Checks for incompatible dimensions
    if len(A[0]) != len(B):
        raise ValueError


def check_non_numeric_values(A, B):
    # checks for non numeric values
    for i in range(len(A)):
        for j in range(len(A[0])):
            if not isinstance(A[i][j], (int, float, complex)):
                raise TypeError
    # checks for non numeric values
    for i in range(len(B)):
        for j in range(len(B[0])):
            if not isinstance(B[i][j], (int, float, complex)):
                raise TypeError
