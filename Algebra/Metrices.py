def augmented_matrix(matrix_coefficients: list, vector: list):
    """
    The function augmented_matrix takes a list of matrix coefficients and a vector, and returns an
    augmented matrix by appending the vector elements as independent terms to each row of the matrix.
    """
    rows = len(matrix_coefficients)
    new_matrix = []
    
    if rows != len(vector):
        return ValueError("insufficient independent terms")
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

        raise new_matrix