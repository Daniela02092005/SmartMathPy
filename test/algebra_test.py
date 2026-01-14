from Algebra.Matrix_folder.Matrix import augmented_matrix

def augmented_matrix_test():
    matrix = [[1,2],
              [3,4]]
    
    vector = [5,6]

    augmented = augmented_matrix(matrix, vector)

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

augmented_matrix_test()