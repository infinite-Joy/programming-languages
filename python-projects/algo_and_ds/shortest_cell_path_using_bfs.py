from collections import deque

def next_cell(grid, row, col, visited):
  # the list is in top, left, bottom, right
  nrow = [-1, 0, 1, 0]
  ncol = [0, -1, 0, 1]
  for rr, cc in zip(nrow, ncol):
    updated_row = row + rr
    updated_col = col + cc
    if 0 <= updated_row < len(grid) and 0 <= updated_col < len(grid[0]):
      if (updated_row, updated_col) not in visited and grid[updated_row][updated_col] == 1:
        yield updated_row, updated_col

def shortestCellPath(grid, sr, sc, tr, tc):
  if len(grid) == 1 and not grid[0]:
    return -1

  queue = deque([((sr, sc), 0)]) # 0,0; level=0
  visited = set((sr, sc))
  while queue:
    (row, col), level = queue.popleft() # 0, 0 level = 0
    if row == tr and col == tc:
      return level
    for nrow, ncol in next_cell(grid, row, col, visited):
      queue.append(((nrow, ncol), level + 1))
      visited.add((nrow, ncol))
  return -1

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
print(shortestCellPath(grid, 0, 0, 2, 0))

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]

print(shortestCellPath(grid, 0, 0, 2, 0))

"""

edge case [[]]

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)

1111
0001
1111

using a bfs should give the shortest path

time complexity m*n
space complexity m*n


queue

while queue is present:
  take the present row , col and the current level
  if target is found: return the level
  iterate on the adj rows and cols that are not already visited:
    append to the queue with level + 1
    add the row , col to the visited
return -1


"""
