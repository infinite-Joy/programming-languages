"""
tjis will be inplace

"""

import numpy as np

def rotate_level(matrix, top, left, bottom, right):
    if top < bottom and left < right:
        for i in range(left, right):
            matrix[top][i], matrix[bottom-i][left] = matrix[bottom-i][left], matrix[top][i]
            matrix[bottom-i][left], matrix[bottom][right-i] = matrix[bottom][right-1], matrix[bottom-i][left]
            matrix[bottom][right-1], matrix[top+i][right] = matrix[top+i][right], matrix[bottom][right-1]
            print(np.array(matrix))
        # rotate_level(matrix, top+1, left+1, bottom-1, right-1)
    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(matrix))
from pprint import pprint
pprint(rotate_level(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1))

# 1   2   3
# 4   5   6
# 7   8   9