import numpy as np
from error import matrixDimensionsMultiplicationError
from models import Matrix

def add_matrices(a: np.array, b: np.array) -> np.array:
    rez = Matrix(r=a.shape[0], c=a.shape[1])
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            rez[i][j] = a[i][j] + b[i][j]
    return rez

def subtract_matrices(a: np.array, b: np.array) -> np.array:
    rez = Matrix(r=a.shape[0], c=a.shape[1])
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            rez[i][j] = a[i][j] - b[i][j]
    return rez

def multiply_matrices(a: np.array, b: np.array) -> np.array:
    if a.shape[1] != b.shape[0] and a.shape[0] != b.shape[1]:
        raise matrixDimensionsMultiplicationError
    rez = Matrix(r=a.shape[0], c=b.shape[1])
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                rez[i][j] += a[i][k] * b[k][j]
    return rez

def scalar_multiplication(a: np.array, scalar: int) -> np.array:
    rez = Matrix(r=a.shape[0], c=a.shape[1])
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            rez[i][j] = scalar * a[i][j]
    return rez


def transpose_matrix(a: np.array) -> np.array:
    rez = Matrix(r=a.shape[1], c=a.shape[0])
    for j in range(a.shape[1]):
        for i in range(a.shape[0]):
            rez[j][i] = a[i][j]
    return rez

def determinant(a: np.array) -> np.array:
    # base case for matrix 1x1
    if len(a) == 1:
        return a[0][0]
    
    # base case for matrix 2x2
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    
    det = 0
    for col in range(len(a)):
        submatrix = np.delete(np.delete(a, 0, axis=0), col, axis=1)  
        cofactor = ((-1) ** col) * a[0][col] * determinant(submatrix)
        det += cofactor
    return det


def inverse(a: np.array) -> np.array:
    if a.shape[0] != a.shape[1]:
        raise ValueError("Matrix is not square")
    
    det_a = determinant(a)
    
    if det_a == 0:
        raise ValueError("Matrix is not invertible")
    rez = Matrix(r=a.shape[0], c=a.shape[1])
    
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            submatrix = np.delete(np.delete(a, i, axis=0), j, axis=1)
            cofactor = ((-1) ** (i + j)) * determinant(submatrix)
            rez[j, i] = cofactor
    return rez / det_a