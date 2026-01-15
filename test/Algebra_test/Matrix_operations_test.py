from Algebra.Matrix_folder.Matrix_operations import matrix_sum, matrix_subtraction, scalar_multiply_matrix, matrix_multiplication

# py -m test.Algebra_test.Matrix_operations_test

print("-----------matrix_sum_test-------------")

def matrix_sum_test():
    A = [[4,2],
         [2,4]]
    
    B = [[3,6],
         [6,3]]
    
    result = matrix_sum(A, B)

    for row in result:
        for element in row:
            print(element, end=" ")
        print()

    # ValueError case
    C = [[1,2],
         [3,4]]
    
    D = [[1,2,3],
         [4,5,6]]

    try:
        result = matrix_sum(C, D)
        print("ERROR: debía fallar y no falló")
    except ValueError:
        print("matrix_sum: The arrays must have the same number of rows and columns")

matrix_sum_test()

print("-----------matrix_subtraction_test-------------")

def matrix_subtraction_test():

    A = [[4,2],
         [2,4]]
    
    B = [[3,6],
         [6,3]]
    
    result = matrix_subtraction(A, B)

    for row in result:
        for element in row:
            print(element, end=" ")
        print()

    # ValueError case
    C = [[1,2],
         [3,4]]
    
    D = [[1,2,3],
         [4,5,6]]

    try:
        result = matrix_subtraction(C, D)
        print("ERROR: debía fallar y no falló")
    except ValueError:
        print("matrix_sum: The arrays must have the same number of rows and columns")

matrix_subtraction_test()

print("-----------scalar_multiply_test-------------")

def scalar_multiply_test():
    A = [[2,2],
         [2,2]]
    
    scalar = 1

    result = scalar_multiply_matrix(A, scalar)

    for row in result:
        for element in row:
            print(element, end=" ")
        print()

    # 0 matrix

    scalar = 0

    result = scalar_multiply_matrix(A, scalar)

    for row in result:
        for element in row:
            print(element, end=" ")
        print()

scalar_multiply_test()

print("-----------matrix_multiplication_test-------------")

def matrix_multiplication_test():
    identity = [[1,0,0],
                [0,1,0],
                [0,0,1]]
    
    A = [[5,2,0],
         [4,8,0],
         [7,6,0]]
    
    result = matrix_multiplication(identity, A)

    for row in result:
        for element in row:
            print(element, end=" ")
        print()

    # Fail case

    B = [[5,6],
         [7,8]]
    
    try:
        result = matrix_multiplication(A, B)
        print("ERROR: debía fallar y no lo hizo")
    except ValueError:
        print("The columns of matrix A must match the rows of matrix B.")

matrix_multiplication_test()