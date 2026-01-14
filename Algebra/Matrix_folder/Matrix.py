def augmented_matrix(matrix_coefficients: list, vector: list):
    """
    The function augmented_matrix takes a list of matrix coefficients and a vector, and returns an
    augmented matrix by appending the vector elements as independent terms to each row of the matrix.
    """
    rows = len(matrix_coefficients)
    new_matrix = []
    
    if rows != len(vector):
        raise ValueError("insufficient independent terms")
    else:
        counter = 0
        for row in matrix_coefficients:
            new_row = []
            for element in row:
                new_row.append(element)
            independent_term = vector[counter]
            new_row.append(independent_term)
            new_matrix.append(new_row)
            counter += 1

        return new_matrix
    
def diagonal(matrix: list):
    """
    The function checks if a given matrix is diagonal. This is based on the definition:
        We say that A is diagonal if it is square and its off-diagonal components are zero.
    """
    rows = len(matrix)
    columns = len(matrix[0])

    diagonal = True

    if rows == columns:
        row_counter = 0
        for row in matrix:
            column_counter = 0
            for element in row:
                if row_counter != column_counter and element != 0:
                    diagonal = False
                    return diagonal
                column_counter += 1
            row_counter += 1
    else:
        diagonal = False

    return diagonal

def identity_matrix(matrix: list):
    """
    The function checks whether a given matrix is an identity matrix by verifying that it is diagonal and has 1 on the main diagonal and 0 
    on the rest. This is based on the definition:
        The identity matrix In is the diagonal matrix of size n whose main diagonal consists of 1's.
    """
    is_diagonal = diagonal(matrix)

    if is_diagonal:
        identity = True
        row_counter = 0
        for row in matrix:
            column_counter = 0
            for element in row:
                if row_counter != column_counter and element != 0:
                    identity = False
                    return identity
                else:
                    if row_counter == column_counter and element != 1:
                        identity = False
                        return identity
                column_counter += 1
            row_counter += 1
    else:
        return False
    
    return identity