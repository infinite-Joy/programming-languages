"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
longest increasing path in a matrix
Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
to do this i think a simple dfs would be good
basically for each cell in the mat: check if already in visited.
if not do a dfs starting from that.
time complexity is O(n2)
space is O(n)
=========================================
"""
from pprint import pprint

class Graph:
    def __init__(self, nums):
        self.nums = nums
        self.visited = set()
        self.processed = set()
        self.max_depth = 0
        self.dim = len(nums), len(nums[0])
        self.memo = {}
    def get_next(self, row, col):
        # check top
        if row-1>=0 and self.nums[row-1][col] > self.nums[row][col]:
            yield row-1, col
        # check bottom
        if row+1<self.dim[0] and self.nums[row+1][col] > self.nums[row][col]:
            yield row+1, col
        # check left
        if col-1>=0 and self.nums[row][col-1] > self.nums[row][col]:
            yield row, col-1
        # check right
        if col+1<self.dim[1] and self.nums[row][col+1] > self.nums[row][col]:
            yield row, col+1
    def dfs(self, height, srow, scol):
        print('height, srow, scol', height, srow, scol, self.visited, self.processed)
        if height == 0:
            self.visited = set()
        self.visited.add((srow, scol))
        if (srow, scol) in self.memo:
            return height+1
        for nrowcol in self.get_next(srow, scol):
            # we dont need the check if nrowcol in visited as this is checked
            # implicitlt, there cannot be a cylce in this as the dfs would not
            # return to the source as source would always be less than all the
            # children
            height = self.dfs(height+1, *nrowcol)
            self.max_depth = max(self.max_depth, self.max_depth + height)
        self.processed.add((srow, scol))
        return self.max_depth

def main(matrix):
    g = Graph(matrix)
    for i in range(g.dim[0]):
        for j in range(g.dim[1]):
            if (i, j) not in g.processed:
                print('starting', i, j)
                g.dfs(0, i, j)
                print('#'*10)
    return g.max_depth + 1


matrix = [[9,9,4],[6,6,8],[2,1,1]]
#matrix = [[7,8,9],[9,7,6],[7,2,3]]
#matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
pprint(matrix)
print(main(matrix))
