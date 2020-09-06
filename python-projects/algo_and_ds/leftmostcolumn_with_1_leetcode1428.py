"""

this looks like a binary value

first is get the dimensions

do a binary search column wise

if 1 not found update the column. if 1 is found then return the column

this will not work. have to go row by row.

"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

from math import inf
class Solution:
    def __init__(self):
        self.mincol = None
    def binary_search(self, binaryMatrix, row, maxcol):
        low = 0
        high = maxcol
        found = False
        while low < high: # 0, 3; 1, 3
            mid = (low + high) // 2
            if binaryMatrix.get(row, mid) == 1:
                high = mid
                found = True
                self.mincol = min(self.mincol, mid)
            else:
                low = mid + 1 # 1, 3; 3, 3;
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        maxrow, maxcol = binaryMatrix.dimensions()
        self.mincol = inf
        for row in range(maxrow):
            self.binary_search(binaryMatrix, row, maxcol)
        if self.mincol is inf:
            return -1
        return self.mincol
