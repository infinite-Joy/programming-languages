"""
We can check if this is the path. by first eliminating all the obstacles in the grid and then introducing the obstacles 1 by 1 and then checking if there is a path between the earlier path and the new path.
read all the obtables
now remove all the obstacles
now do bfs and take note of the path
then introduce the obstacles one by one and see if there is a workaround available

from collections import deque
class Solution:
    def read_obstacles(self, grid, rowsize, colsize):
        obstacles = []
        for row in len(rowsize):
            for col in len(colsize):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    obstacles.append((row, col))
        return set(obstacles)
    def next_cell(self, grid, row, col):
        rowdir = [-1, 0, 1, 0]
        coldir = [0, -1, 0, 1]
        for deltarow, deltacol in zip(rowdir, coldir):
            nrow = row + deltarow
            ncol = col + deltacol
            if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                yield nrow, ncol
    def bfs(self, grid, start, end):
        path = []
        queue = deque([(start, path)])
        visited.add(start)
        while queue:
            (row, col), path = queue.popleft()
            if row == end[0] and col == end[1]:
                return path
            for nrow, ncol in self.next_cell(grid, row, col):
                newpath = path[::]
                newpath.append((row, col))
                queue.append(((nrow, ncol), newpath))
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        obstacles = self.read_obstacles(grid, rowsize, colsize)
spath = self.bfs(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))
for obstacle in obstacles:
    row, col = obstacle
    grid[row][col] = 1
    if (row, col) in starting_path[:-k]:
        remove_index = path.index((row, col))
        start = path[remove_index - 1]
        end = path[remove_index + 1]
        workaround = self.bfs(grid, start, end)
        path = path[:start + 1] + wordaround + path[:start + 2]
return len(path)

"""

from collections import deque
from typing import List
class Solution:
    def read_obstacles(self, grid, rowsize, colsize):
        obstacles = []
        for row in range(rowsize):
            for col in range(colsize):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    obstacles.append((row, col))
        return obstacles
    def next_cell(self, grid, row, col):
        rowdir = [-1, 0, 1, 0]
        coldir = [0, -1, 0, 1]
        for deltarow, deltacol in zip(rowdir, coldir):
            nrow = row + deltarow
            ncol = col + deltacol
            if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                if grid[nrow][ncol] != 1:
                    yield nrow, ncol
    def bfs(self, grid, start, end):
        path = []
        queue = deque([(start, path)])
        visited = set()
        visited.add(start)
        while queue:
            (row, col), path = queue.popleft()
            print(path)
            if row == end[0] and col == end[1]:
                return path
            for nrow, ncol in self.next_cell(grid, row, col):
                if (nrow, ncol) not in visited:
                    newpath = path[::]
                    newpath.append((row, col))
                    queue.append(((nrow, ncol), newpath))
                    visited.add((nrow, ncol))
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        obstacles = self.read_obstacles(grid, len(grid), len(grid[0]))
        print(obstacles)
        print(grid)
        path = self.bfs(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))
        for obstacle in obstacles[:-k]:
            row, col = obstacle
            grid[row][col] = 1
            print(row, col)
            if (row, col) in path:
                remove_index = path.index((row, col))
                start = path[remove_index - 1]
                end = path[remove_index + 1]
                print(start, end)
                workaround = self.bfs(grid, start, end)
                print(path, workaround)
                path = path[:remove_index] + workaround + path[remove_index + 1:]
                print(path)
        return len(path)

grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]
k = 1
sol = Solution()
print(sol.shortestPath(grid, k))
