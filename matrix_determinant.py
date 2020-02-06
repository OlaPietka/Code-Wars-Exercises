import numpy as np

def determinant(matrix):
    if len(matrix) == 1: return matrix[0][0]
    if len(matrix) == 2: return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    det = [(e if i % 2 == 0 else -e)*determinant(np.delete(np.delete(matrix, 0, 0), i, 1)) for i, e in enumerate(matrix[0])]
    return sum(det)