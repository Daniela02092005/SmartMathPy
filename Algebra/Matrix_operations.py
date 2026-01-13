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
        Suppose that A=[ai,j] is a matrix in Mmxn and c∈R (a scalar). 
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

def matrix_multiplication(A_matrix: list, B_matrix: list):
    """
    The function performs matrix multiplication between two matrices A and B, returning the result if the columns of A match the rows of B; 
    otherwise, it generates a ValueError error. This is based on the definition:
        Let A be an mxn matrix and B an nxp matrix. The entry ij of AB is calculated by multiplying row i of A by column j of B.
        The entry ij of AB is given by:
            (AB)ij = ai1b1j + ai2b2j+...+ainbnj; where 1,2,...,n = k and ABmxp.
    """
    A_columns = len(A_matrix[0])
    B_rows = len(B_matrix)

    rows = len(A_matrix)
    columns = len(B_matrix[0])

    result = [[0 for _ in range(columns)] for _ in range(rows)]

    if A_columns == B_rows:
        for i in range(rows):
            for j in range(columns):
                for k in range(A_columns):
                    result[i][j] += A_matrix[i][k] * B_matrix[k][j]
        return result
    else:
        raise ValueError("The columns of matrix A must match the rows of matrix B.")

def transposed_matrix(matrix: list):
    """
    The transposed_matrix function takes a matrix as input and returns its transpose. This is based on the definition:
        Let Amxn be an mxn matrix. The transpose of A, denoted A^T, is the nxm matrix whose ij component is the ji component of A. That is, 
        Aij = Aji.
        In other words, A^T is obtained by swapping rows and columns of A.
    """
    rows = len(matrix)
    columns = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix[i][j]
    
    return result

def submatrix(matrix: list, i: int, j: int):
    """
    The function `submatrix` takes a matrix and two indices `i` and `j`, and returns a submatrix by
    excluding the i-th row and j-th column. 
    """
    
    submatrix = []
    row_counter = 0
    for row in matrix:
        if row_counter != i:
            new_row = []
            column_counter = 0
            for element in row:
                if column_counter != j:
                    new_row.append(element)
                column_counter += 1
            submatrix.append(new_row)
        row_counter += 1
        
    return submatrix