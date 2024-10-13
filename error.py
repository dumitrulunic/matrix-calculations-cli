class matrixDimensionsError(Exception):
    def __init__(self, message="The matrices have different dimensions"):
        self.message = message
        super().__init__(self.message)
        
class matrixDimensionsMultiplicationError(Exception):
    def __init__(self, message="The matrices have non-matching dimensions for multiplication"):
        self.message = message
        super().__init__(self.message)