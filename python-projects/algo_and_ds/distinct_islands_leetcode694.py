"""

find the distinct islands.

this is a connected components soltution

but what we can do is that

we can take the rows make it all 0 and then add the nubers
in this way we will capture the geometru

and then convert that to a string and store all the geometries

that way we will know the distinct islands

"""

from collections import deque
from typing import List
class Solution:
    def next_cell(self, grid, row, col):
        row_dir = [-1, 0, 1, 0]
        row_col = [0, -1, 0, 1]

        for deltarow, deltacol in zip(row_dir, row_col):
            nrow = row + deltarow
            ncol = row + deltacol
            if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                if grid[nrow][ncol] == 1:
                    yield nrow, ncol
    def bfs(self, grid, row, col, islands):
        island_hash = [0 for _ in grid[0]]
        queue = deque([(row, col)])
        grid[row][col] = 0
        island_hash[col] += 1
        while queue:
            row, col = queue.popleft()
            for nrow, ncol in self.next_cell(grid, row, col):
                queue.append((nrow, ncol))
                grid[nrow][ncol] = 0
                island_hash[ncol] += 1
        island_hash = list(filter(lambda x: x > 0, island_hash))
        islands.add(tuple(island_hash))

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.bfs(grid, row, col, islands)
                    print(islands)
        return len(islands)

# test case
arr = [[1,1,0,1,1], [1,0,0,0,0], [0,0,0,0,1], [1,1,0,1,1]]
import numpy as np
print(np.matrix(arr))
sol = Solution()
print(sol.numDistinctIslands(arr))
