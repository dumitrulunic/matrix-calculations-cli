import numpy as np
import ast

class Matrix:
    def __init__(self, r, c) -> np.array:
        self.matrix = np.zeros((r, c))
        self.columns = c
        self.rows = r
        
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __setitem__(self, index, value):
        self.matrix[index] = value
    
    def __repr__(self):
        return str(self.matrix)
    
    def _from_array(self, arr):
        # Helper method to set the matrix from a NumPy array
        self.matrix = arr
        return self
    
    def __truediv__(self, scalar):
    # Division by a scalar: divide each element of the matrix by the scalar
        return Matrix(r=self.rows, c=self.columns)._from_array(self.matrix / scalar)
    
    def matrix_from_input(self):
        print("Please enter the matrix as a list of lists", color="yellow")
        self.matrix = ast.literal_eval(input())
        self.matrix = np.array(self.matrix)