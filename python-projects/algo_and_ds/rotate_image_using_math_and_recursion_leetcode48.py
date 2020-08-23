"""
maybe the matrix rotation can be used and then some simple problems

(0 0, 0, len) (0 1, 1, len) (0, 2, 2, len)
(1 0, 0, len-1) (1 1 1 len-1)


[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

i can do a recursive soltuon that will do the rotation for the current shell
in each recursion will be implementing for the current row

recursion for the current layer

for loop on the elem

then do the roation and go to the next elem

complexity is O(n*m)



"""

from typing import List

def cell_rotation_dfs(matrix, startrow, startcol, row, col):
    if row == startrow and col == startcol:
        return

    matrix[startrow][startcol], matrix[row][col] = matrix[row][col], matrix[startrow][startcol]
    #nrow, ncol = col, len(matrix) - row
    cell_rotation_dfs(matrix, startrow, startcol, col, len(matrix) - row - 1)

def do_cell_rotation(matrix, leftupper_row, leftupper_col, rightlower_row, rightlower_col):
    for col in range(leftupper_col, rightlower_col):
        cell_rotation_dfs(matrix, leftupper_row, col, col, len(matrix) - leftupper_row - 1)

def iterate_on_layer(matrix, leftupper_row, leftupper_col, rightlower_row, rightlower_col):
    if leftupper_row >= rightlower_row or leftupper_col >= rightlower_col:
        return
    #print(leftupper_row, leftupper_col, rightlower_row, rightlower_col)
    do_cell_rotation(matrix, leftupper_row, leftupper_col, rightlower_row, rightlower_col)
    iterate_on_layer(matrix, leftupper_row+1, leftupper_col+1, rightlower_row-1, rightlower_col-1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        iterate_on_layer(matrix, 0, 0, len(matrix)-1, len(matrix)-1)

import numpy
s = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(numpy.matrix(matrix))
#cell_rotation_dfs(matrix, 0, 0, 0, 3)
#do_cell_rotation(matrix, 0, 0, 3, 3)
#iterate_on_layer(matrix, 0, 0, 3, 3)
s.rotate(matrix)

print(numpy.matrix(matrix))
