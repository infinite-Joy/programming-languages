#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
# this is solved using a simple dfs.
# we basically iterate on the graph and then do a dfs.
# and then we keep an maximum counter to this
# once done we find the maximum value
from pprint import pprint
import numpy


class Grid:
    def __init__(self, g):
        self.g = g
        self.visited = set()
        self.cells = 0
    def next_cell(self, row, col):
        # both up down left right and diagonals are allowed
        row_dirs = [-1, -1, 0, 1, 1, 1, 0, -1]
        col_dirs = [0, -1, -1, -1, 0, 1, 1, 1]
        for rr, cc in zip(row_dirs, col_dirs):
            nrow = row + rr
            ncol = col + cc
            #print(row, col, nrow, ncol, rr, cc)
            if 0 <= nrow < len(self.g) and 0 <= ncol < len(self.g[0]):
                if self.g[nrow][ncol] == 1:
                    yield nrow, ncol
    def dfs(self, row, col):
        self.cells += 1
        self.visited.add((row, col))
        for nrow, ncol in self.next_cell(row, col):
            if (nrow, ncol) not in self.visited:
                self.dfs(nrow, ncol)

def maxRegion(grid):
    maxcells = 0
    g = Grid(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                if (row, col) not in g.visited:
                    g.dfs(row, col)
                    maxcells = max(maxcells, g.cells)
                    print(row, col, g.cells, maxcells, g.visited)
                    g.cells = 0
    return maxcells

#grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
grid = [[0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 0, 1, 0], [0, 1, 0, 1, 1], [0, 1, 1, 1, 0]]
print(numpy.matrix(grid))
print(maxRegion(grid))
