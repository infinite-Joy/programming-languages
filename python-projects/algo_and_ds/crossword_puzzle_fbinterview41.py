#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the crosswordPuzzle function below.
# simple one would be a backtracking problem.
# and pruning.
# this looks like a graph coloring problem. where the
# groups of contiguous - are the nodes if tehre is a -
# connected between the two then there is an edge.
# and then probably a backtracking problem can be done
# this is like a tree

def grid_moves(grid, row, col):
    moverow = [-1, 0, 1, 0]
    movecol = [0, -1, 0, 1]
    for mover, movec in zip(moverow, movecol):
        if 0 <= row+mover < len(grid):
            if 0 <= col+movec < len(grid[0]):
                if grid[row+mover][col+movec] == '-':
                    yield row+mover, col+movec

def grid_dfs(grid, row, col, string, stringidx, prevrow=None, prevcol=None, visited=None):
    if visited is not None:
        visited.add((row, col))
    else:
        visited = set([(row, col)])
    for nrow, ncol in grid_moves(grid, row, col):
        if (nrow, ncol) not in visited:
            if (prevcol - row == row - nrow) or (prevcol - col == col - ncol):
                grid[row][col] = string[stringidx]
                grid_dfs(grid, nrow, ncol, string, stringidx+1, row, col, visited)
                grid[row][col] = '-'

def first_space(grid):
    for rowidx, rowel in enumerate(grid):
        for colidx, elem in enumerate(rowel):
            if elem == '-':
                return rowidx, colidx

def crosswordPuzzle(crossword, words):
    crossword = [list(g) for g in crossword]
    words = words.split(';')
    first_space
