from Algebra.Matrix_folder.Matrix import augmented_matrix, diagonal, identity_matrix

def augmented_matrix_test():
    matrix = [[1,2],
              [3,4]]
    
    vector = [5,6]

    augmented = augmented_matrix(matrix, vector)

    for row in augmented:
        for element in row:
            print(element, end=" ")
        print()

    # Fail case
    matrix = [[1,2],
              [3,4]]
    
    vector = [5,6,7]

    try:
        augmented = augmented_matrix(matrix, vector)
        print("ERROR: debía fallar y no falló")
    except ValueError:
        print("augmented_matrix: error correctamente detectado")

print("----------------------------------------------------------------")

augmented_matrix_test()

def diagonal_test():
    true_matrix = [[1,0,0],
                   [0,2,0],
                   [0,0,3]]
    
    result = diagonal(true_matrix)

    print(result)

    # False case
    false_matrix = [[1,1,0],
                    [0,2,0],
                    [0,0,3]]
    
    result = diagonal(false_matrix)

    print(result)

    # Second false case (non-square matrix)
    non_square = [[1,1,1,1],
                  [2,2,2,2],
                  [3,3,3,3]]
    
    result = diagonal(non_square)

    print(result)

print("----------------------------------------------------------------")

diagonal_test()

def identity_test():
    true_matrix = [[1,0,0],
                   [0,1,0],
                   [0,0,1]]
    
    result = identity_matrix(true_matrix)

    print(result)

    # False case
    false_matrix = [[2,0,0],
                    [0,3,0],
                    [0,0,4]]
    
    result = identity_matrix(false_matrix)

    print(result)

print("----------------------------------------------------------------")

identity_test()