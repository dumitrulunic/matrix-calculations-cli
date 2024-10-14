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
    

    