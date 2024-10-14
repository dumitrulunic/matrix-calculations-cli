import numpy as np
import ast
from error import matrixDimensionsError
from operations import add_matrices, subtract_matrices, multiply_matrices, scalar_multiplication, transpose_matrix, determinant
from print_color import print

def one_matrix():
    print("Please enter the matrix as a list of lists", color="yellow")
    matrix = ast.literal_eval(input())
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        raise ValueError("Please enter a 2D matrix")
    return matrix
    
def two_matrices():
    print("Please enter the first matrix as a list of lists", color="yellow")
    matrix_1 = ast.literal_eval(input())
    print("Please enter the second matrix as a list of lists", color="yellow")
    matrix_2 = ast.literal_eval(input())
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)
    if matrix_1.ndim != 2 or matrix_2.ndim != 2:
        raise ValueError("Please enter a 2D list")
    return matrix_1, matrix_2

def start():
    operations = {
        1: "Addition",
        2: "Substraction",
        3: "Multiplication",
        4: "Scalar Multiplciation",
        5: "Transpose",
        6 : "Determinant",
    }
    print("Hello, what kind of operation do you need?")
    for key, value in operations.items():
        print(f"{key}: {value}")
    operation_num = int(input("Enter your choice: "))
    
    if operation_num == 1:
        matrix_1, matrix_2 = two_matrices()
        result = add_matrices(matrix_1, matrix_2)
        print("The result is: \n")
        print(result, color="green")
        
    elif operation_num == 2:
        matrix_1, matrix_2 = two_matrices()
        result = subtract_matrices(matrix_1, matrix_2)
        print("The result is: \n")
        print(result, color="green")
        
    elif operation_num == 3:
        matrix_1, matrix_2 = two_matrices()
        result = multiply_matrices(matrix_1, matrix_2)
        print("The result is: \n")
        print(result, color="green")
        
    elif operation_num == 4:
        matrix = one_matrix()
        print("Please enter the scalar", color="yellow")
        scalar = int(input())
        result = scalar_multiplication(matrix, scalar)
        print("The result is: \n")
        print(result, color="green")
    elif operation_num == 5:
        matrix = one_matrix()
        result = transpose_matrix(matrix)
        print("The result is: \n")
        print(result, color="green")
    elif operation_num == 6:
        matrix = one_matrix()
        result = determinant(matrix)
        print("The result is: \n")
        print(result, color="green")
        

          
    

if __name__ == "__main__":
    start()
    
    