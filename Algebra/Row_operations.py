def swap_rows(matrix: list, first_index: int, second_index: int):
    """
    The `swap_rows` function takes a matrix and two row indices, and swaps the rows at those indices in the array.
    This is based on the definition:
        We will distinguish three types of operations between rows of a matrix, which we will call elementary row operations:
        1. Swap two of its rows: This operation will be indicated with the symbol Ri ↔Rj, which means that we swap rows i and j of the matrix.
    """

    matrix[first_index], matrix[second_index] = matrix[second_index], matrix[first_index]
    return matrix

def multiply_by_a_scalar(matrix: list, row_index: int, scalar):

    if scalar != 0:
        new_matrix = []
        counter = 0
        for row in matrix:
            new_row = []
            for element in row:
                if counter == row_index:
                    obj = element * scalar
                    new_row.append(obj)
                else:
                    new_row.append(element)
            new_matrix.append(new_row)
            counter += 1
        return new_matrix
    else:
        raise ValueError("The scalar must be different to 0.")