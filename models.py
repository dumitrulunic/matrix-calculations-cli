import numpy as np
import ast

class Matrix:
    def __init__(self, r, c) -> np.array:
        self.matrix = np.zeros((r, c))
        self.columns = c
        self.rows = r
        
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __repr__(self):
        return str(self.matrix)
    
    def matrix_from_input(self):
        print("Please enter the matrix as a list of lists", color="yellow")
        self.matrix = ast.literal_eval(input())
        self.matrix = np.array(self.matrix)