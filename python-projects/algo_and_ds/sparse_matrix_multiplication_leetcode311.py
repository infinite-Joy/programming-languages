"""

sparse matrix multiplication

leetcode 311

we can convert the dense matrix to a sparse matrix

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |


sparse_a[0] = {0: 1, 1: 1, 2: 1}
sparse_a[1] = {0: -1, 2: 3}

in the real world we should have in both the directions

time complexity: O(number of valid elements)
space complexity: O(number of valid elements)

"""

from typing import List

class SparseMatrix:
    def __init__(self, rowcol, colrow):
        self.rowcol = rowcol
        self.colrow = colrow
    @classmethod
    def from_dense(cls, dense_mat):
        rowcol = {}
        colrow = {}
        rows = len(dense_mat)
        cols = len(dense_mat[0])
        for row in range(rows):
            for col in range(cols):
                if dense_mat[row][col] != 0:
                    if row not in rowcol:
                        rowcol[row] = {}
                    rowcol[row][col] = dense_mat[row][col]
                    if col not in colrow:
                        colrow[col] = {}
                    colrow[col][row] = dense_mat[row][col]
        return cls(rowcol, colrow)
    @staticmethod
    def to_dense(dim, rowcol):
        mat = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
        for row in rowcol:
            for col in rowcol[row]:
                mat[row][col] = rowcol[row][col]
        return mat
    def multiply(self, other):
        solrowcol = {}
        maxrow, maxcol = 0, 0
        maxrow = max(self.rowcol.keys())
        maxcol = max(other.rowcol.keys())
        for row1 in self.rowcol:
            for col1 in self.rowcol[row1]:
                # things get reversed in the other case
                row2 = col1
                col2 = row1
                if row2 in other.rowcol and col2 in other.rowcol[row2]:
                    if row1 not in solrowcol:
                        solrowcol[row1] = {}
                        if col2 not in solrowcol[row1]:
                            solrowcol[row1][col2] = 0
                    solrowcol[row1][col2] += self.rowcol[row1][col1] * other.rowcol[row2][col2]

        return (maxrow+1, maxcol+1), solrowcol

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        sparse_a = SparseMatrix.from_dense(A)
        print(sparse_a.rowcol)
        sparse_b = SparseMatrix.from_dense(B)
        print(sparse_b.colrow)
        dim, solrowcol = sparse_a.multiply(sparse_b)
        print(dim, solrowcol)
        return SparseMatrix.to_dense(dim, solrowcol)

# test cases
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
import numpy as np
print(np.matrix(A))
print(np.matrix(B))
sol = Solution()
print(np.matrix(sol.multiply(A, B)))
