"""
tjis will be inplace

"""

import numpy as np

# def rotate_level(matrix, top, left, bottom, right):
#     if top < bottom and left < right:
#         for i in range(left, right):
#             matrix[top][i], matrix[bottom-i][left] = matrix[bottom-i][left], matrix[top][i]
#             matrix[bottom-i][left], matrix[bottom][right-i] = matrix[bottom][right-1], matrix[bottom-i][left]
#             matrix[bottom][right-1], matrix[top+i][right] = matrix[top+i][right], matrix[bottom][right-1]
#             print(np.array(matrix))
#         # rotate_level(matrix, top+1, left+1, bottom-1, right-1)
#     return matrix


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(np.array(matrix))
# from pprint import pprint
# pprint(rotate_level(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1))

# 1   2   3
# 4   5   6
# 7   8   9

#############################
# the idea is to first transpose the matrix
# and then flip the matrix once that is done

# common method for swapping the symmetry
# point is that this is a square matrix

# in this case we are doing clockwise rotation

# https://leetcode.com/problems/rotate-image/

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def swap_symmetry_rotate_clockwise(matrix):
    # rotate along vertical axis
    colend = len(matrix[0]) - 1
    for col in range(int(len(matrix[0])/2)):
        for row in range(len(matrix)):
            # print(row, col, colend-row)
            matrix[row][col], matrix[row][colend-col] = matrix[row][colend-col], matrix[row][col]
    return matrix



def rotate_level(matrix):
    matrix = transpose(matrix)
    print(np.array(matrix))
    matrix = swap_symmetry_rotate_clockwise(matrix)
    print(np.array(matrix))
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(matrix))
print(rotate_level(matrix))



"""
implement an opposite swapping. this can mimic the rotation



"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        def swap_symmetry_rotate_clockwise(matrix):
            # rotate along vertical axis
            colend = len(matrix[0]) - 1
            for col in range(int(len(matrix[0])/2)):
                for row in range(len(matrix)):
                    # print(row, col, colend-row)
                    matrix[row][col], matrix[row][colend-col] = matrix[row][colend-col], matrix[row][col]
            return matrix

        def rotate_level(matrix):
            matrix = transpose(matrix)
            # print(np.array(matrix))
            matrix = swap_symmetry_rotate_clockwise(matrix)
            # print(np.array(matrix))
            return matrix
        
        return rotate_level(matrix)