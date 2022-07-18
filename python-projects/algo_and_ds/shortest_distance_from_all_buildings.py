"""
naive solution
for each empty lot. compute the distance to all the buildings
find the minimum value. report that
probably a combination of bfs and memoisation

"""

import math
from collections import deque
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(grid, row, col):
            distances = []
            queue = deque([[row, col, 0]])
            visited = {}
            while queue:
                # print(queue)
                cellrow, cellcol, d = queue.popleft()
                if grid[cellrow][cellcol] == 1:
                    distances.append(d)
                elif grid[cellrow][cellcol] == 2:
                    pass
                else:
                    for rowdiff, coldiff in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        newrow = cellrow + rowdiff
                        newcol = cellcol + coldiff
                        if (newrow, newcol) not in visited and 0 <= newrow < len(grid) and 0 <= newcol < len(grid[0]):
                            queue.append([newrow, newcol, d+1])
                            visited[(newrow, newcol)] = True
            return distances
            
        def get_min_distance(grid):
            min_dist = math.inf
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 0: # this is a empty
                        distances = bfs(grid, row, col)
                        min_dist = min(min_dist, sum(distances))
            if min_dist == math.inf: return -1
            return min_dist
        
        return get_min_distance(grid)

import math
from collections import deque
from typing import List

def bfs(grid, row, col, total_buildings):
    distances = []
    queue = deque([[row, col, 0]])
    visited = {}
    while queue:
        # print(queue)
        cellrow, cellcol, d = queue.popleft()
        if grid[cellrow][cellcol] == 1:
            distances.append(d)
        elif grid[cellrow][cellcol] == 2:
            pass
        else:
            for rowdiff, coldiff in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newrow = cellrow + rowdiff
                newcol = cellcol + coldiff
                if (newrow, newcol) not in visited and 0 <= newrow < len(grid) and 0 <= newcol < len(grid[0]):
                    queue.append([newrow, newcol, d+1])
                    visited[(newrow, newcol)] = True
    # print(f'{distances=}')
    if len(distances) < total_buildings:
        return []
    return distances
    
def get_min_distance(grid):
    min_dist = math.inf
    total_buildings = 0
    # find the total number of buildings
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                total_buildings += 1
    # now do the distance search
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0: # this is a empty
                # print(f'{row=}, {col=}')
                distances = bfs(grid, row, col, total_buildings)
                # print(distances)
                if distances:
                    min_dist = min(min_dist, sum(distances))
    if min_dist == math.inf: return -1
    return min_dist

# grid = [[1,2,0]]
# print(get_min_distance(grid))

import numpy as np
# grid = [[0,2,1],[1,0,2],[0,1,0]]
# print(np.array(grid))
# print(get_min_distance(grid))

grid = [[2,0,0,2,2,0,2,0,1,0,0,0,2,2,0,0,2,0,2,2,2,2,1,0,0],[0,0,0,0,0,1,2,0,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0],[2,2,0,2,0,1,2,0,0,0,0,2,2,0,2,2,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,2,2,2,2,2,1,2,2,2,0,0,0,0,2,2,0,2,2],[2,0,2,0,2,2,0,0,2,0,0,2,0,0,2,0,0,0,1,0,0,0,0,0,2],[0,2,2,0,2,2,1,0,2,2,1,0,2,0,0,2,0,1,0,0,0,2,2,2,0],[2,0,2,2,2,0,2,0,2,1,0,2,0,0,2,0,0,0,0,0,0,0,0,2,2],[0,2,2,0,0,2,2,0,0,2,0,0,0,0,2,0,2,2,0,2,0,0,2,1,0],[0,2,0,2,0,2,2,0,2,0,2,0,0,0,2,0,0,1,2,2,0,2,2,0,0],[2,2,0,0,0,0,0,2,0,0,0,0,0,2,2,1,2,2,2,0,0,1,2,0,0],[0,0,0,0,0,2,2,0,2,2,2,1,0,0,2,0,0,0,0,2,0,2,0,0,0],[2,0,0,2,0,2,0,0,0,2,0,0,2,2,0,2,0,0,0,0,2,0,0,0,0],[2,0,0,0,0,2,1,2,0,0,0,2,0,2,2,0,0,1,0,2,0,2,0,2,1],[0,0,0,2,0,0,2,2,1,0,2,0,0,2,2,0,2,2,0,0,0,2,0,2,2],[0,0,0,0,2,0,0,0,2,0,2,0,2,2,0,0,2,0,0,0,0,0,0,0,0],[0,1,2,0,0,0,0,2,2,0,0,0,1,2,0,2,2,0,0,0,0,0,0,2,0],[2,2,2,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,2,2,0,2,2],[0,0,2,0,1,2,0,2,0,1,0,0,2,0,2,0,2,2,0,2,2,0,0,0,2],[0,0,2,0,0,0,2,2,0,0,0,2,0,2,2,0,0,0,2,2,2,2,0,0,2],[2,0,2,0,2,0,0,1,2,0,0,0,2,1,2,0,2,2,0,0,2,2,2,0,0],[0,0,0,0,0,0,2,0,0,2,0,0,2,2,0,2,2,0,0,2,1,0,2,2,2],[2,1,0,0,2,0,0,0,1,0,2,0,2,0,0,2,0,2,0,0,0,0,2,0,2],[2,0,1,0,1,0,0,0,0,0,1,2,2,0,0,2,2,0,2,0,0,0,2,2,0],[0,0,2,2,0,2,2,2,2,0,0,2,0,1,0,0,0,2,2,0,0,1,1,2,2],[0,0,0,2,0,0,0,2,0,2,0,2,2,2,0,0,0,2,2,0,0,2,0,0,0],[2,0,2,0,0,2,0,0,2,2,0,0,2,0,0,0,2,2,0,2,2,2,0,2,0],[2,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,0,1,0,0,2,0,0,2,0],[0,0,2,0,0,2,0,0,2,2,0,1,0,0,0,0,2,0,1,2,0,0,0,2,2],[2,0,2,0,1,2,0,0,0,2,1,0,0,0,0,0,1,2,0,2,0,0,2,0,0],[0,2,2,2,2,0,2,0,2,0,2,0,0,2,2,0,0,0,0,0,2,0,1,2,2],[2,0,1,0,2,0,2,0,0,2,2,0,2,0,2,2,2,2,0,2,2,1,0,0,2],[2,2,2,0,2,0,2,2,0,0,0,0,0,0,2,0,0,0,0,2,2,0,2,2,2],[0,0,2,0,2,0,2,0,2,2,2,2,2,1,0,2,2,0,0,0,2,0,0,2,0],[2,0,2,2,0,0,0,2,2,0,2,2,0,2,2,2,0,0,0,0,0,2,1,0,2],[0,0,0,0,0,2,0,0,2,2,2,2,0,0,0,0,2,2,2,2,0,0,0,0,0],[0,2,2,0,0,2,0,0,0,2,0,2,0,0,0,2,0,0,0,0,0,0,2,2,0],[0,0,0,1,0,2,0,2,0,2,0,0,0,0,1,2,0,0,0,0,1,0,0,2,0],[0,2,0,0,2,0,0,0,2,0,1,0,2,0,0,0,0,0,2,0,1,0,0,0,1],[2,0,1,0,0,2,0,0,0,2,2,0,0,0,0,0,0,0,1,0,0,0,2,0,0],[0,0,2,0,0,1,1,0,0,2,2,2,0,2,0,2,1,2,0,1,2,2,2,0,0],[1,0,2,2,0,2,0,0,0,2,2,0,1,2,0,0,0,2,0,2,2,0,1,2,0],[1,0,2,2,2,0,0,0,2,2,2,0,0,2,0,2,0,2,0,2,0,2,2,0,0],[2,0,2,2,2,2,0,2,2,0,0,0,2,0,1,0,2,0,0,0,0,2,2,0,2],[2,0,2,0,0,1,0,2,2,2,1,0,0,2,0,2,2,2,0,2,2,2,2,0,0],[2,0,0,0,0,1,0,0,0,0,0,0,2,0,1,2,0,2,1,0,0,0,0,0,2],[2,0,2,1,2,0,2,0,2,0,2,0,2,1,2,2,0,2,0,2,2,0,2,0,0],[2,0,0,2,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,2,0,2,2,0,0],[2,2,0,0,0,2,0,2,1,0,0,2,2,2,0,2,2,0,0,2,0,2,0,0,2],[0,0,0,0,0,2,2,0,2,0,0,0,0,2,2,0,0,0,0,0,2,0,0,0,0]]
print(np.array(grid))
print(get_min_distance(grid))
