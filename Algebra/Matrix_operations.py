def matrix_sum(matrix_A: list, matrix_B: list):
    """
    The `matrix_sum` function takes two matrices as input and returns the sum of their elements if they have the same number of rows and 
    columns; otherwise, it generates a ValueError error. This is based on the definition:
        Suppose that A = [ai,j] and B = [bi,j] are Mmxn matrices. Their sum A+B is the Mmxn matrix obtained by adding the corresponding 
        components of each matrix.
    """

    rows_A = len(matrix_A)
    rows_B = len(matrix_B)
    columns_A = len(matrix_A[0])
    columns_B = len(matrix_B[0])

    if rows_A == rows_B and columns_A == columns_B:
        result = []

        row_counter = 0
        for row in matrix_A:
            new_row = []
            column_counter = 0
            for element in row:
                obj = element + matrix_B[row_counter][column_counter]
                new_row.append(obj)
                column_counter += 1
            result.append(new_row)
            row_counter += 1

        return result
                
    else:
        raise ValueError("The arrays must have the same number of rows and columns")
    
def matrix_subtraction(matrix_A: list, matrix_B: list):
    """
    The `matrix_subtraction` function takes two matrices as input and returns the subtraction of their elements if they have the same number 
    of rows and columns; otherwise, it generates a ValueError error. This is based on the definition:
        Suppose that A = [ai,j] and B = [bi,j] are Mmxn matrices. Their subtraction A-B is the Mmxn matrix obtained by adding the 
        corresponding components of each matrix.
    """

    rows_A = len(matrix_A)
    rows_B = len(matrix_B)
    columns_A = len(matrix_A[0])
    columns_B = len(matrix_B[0])

    if rows_A == rows_B and columns_A == columns_B:
        result = []

        row_counter = 0
        for row in matrix_A:
            new_row = []
            column_counter = 0
            for element in row:
                obj = element - matrix_B[row_counter][column_counter]
                new_row.append(obj)
                column_counter += 1
            result.append(new_row)
            row_counter += 1

        return result
                
    else:
        raise ValueError("The arrays must have the same number of rows and columns")
    
def scalar_multiply_matrix(matrix: list, scalar):
    """
    The scalar_multiply_matrix function multiplies each element of a matrix by a scalar value and returns the resulting matrix. This is based 
    on the definition:
        Suppose that A=[ai,j] is a matrix in Mmxn and c∈ℝ (a scalar). 
        Then c*A is the matrix in Mmxn obtained by multiplying each component of A by c: c*A=[cai,j]
    """
    result = []

    for row in matrix:
        new_row = []
        for element in row:
            obj = element * scalar
            new_row.append(obj)
        result.append(new_row)

    return result