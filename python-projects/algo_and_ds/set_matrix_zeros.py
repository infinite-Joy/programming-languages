"""
create a arr of row and cols
get the multiplication of the rows and cols
whichever is 0 make it 0


"""

import operator
from functools import reduce


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        this is an O(n+m) space solution
        """
        rows = [1] * len(matrix)
        cols = [1] * len(matrix[0])
        for i, r in enumerate(matrix):
            rows[i] = reduce(operator.mul, r, 1)
        for i, c in enumerate(matrix[0]):
            cols[i] = reduce(lambda x, y: operator.mul(x, y[i]), matrix, 1)
            
        # make all rows 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if rows[r] == 0 or cols[c] == 0:
                    matrix[r][c] = 0
                    
        return matrix


def set_zeros(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0 or matrix[r][0] == 0::
                matrix[r][c] = 0
    return matrix