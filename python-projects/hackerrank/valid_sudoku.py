"""
https://leetcode.com/problems/valid-sudoku/
check if a sudoku is valid or not
this can probably be done
so all the nums in the same cell are the neighbors and
the nums in the same row and col are the neighbors
row = 4
col = 4
complexity: O(n2)
=====================================
"""

from typing import List
from pprint import pprint

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.visited = set()
        self.processed = set()
    def get_neighbors(self, row, col):
        start_row = int(row/3)*3
        start_col = int(col/3)*3
        # sub  box
        for sub_row in range(start_row, start_row+3):
            for sub_col in range(start_col, start_col+3):
                if self.board[sub_row][sub_col] != "." and sub_row!=row and sub_row!=col:
                    yield sub_row, sub_col
        # get rows
        for r in range(self.size):
            if r != row and self.board[r][col] != ".":
                yield r, col
        # get cols
        for c in range(self.size):
            if c != col and self.board[row][c] != ".":
                yield row, c
    def process_edge(self, row1, col1, row2, col2):
        #print('process_edge', row1, col1, row2, col2)
        if self.board[row1][col1] < "0" or self.board[row1][col1] > "9":
            return False
        if self.board[row2][col2] < "0" or self.board[row2][col2] > "9":
            return False
        if self.board[row1][col1] == self.board[row2][col2]:
            return False
        return True
    def dfs(self, row=0, col=0):
        #print(row, col)
        self.visited.add((row, col))
        for neighbor in self.get_neighbors(row, col):
            #print(row, col, neighbor)
            if neighbor not in self.visited:
                row2, col2 = neighbor
                if self.process_edge(row, col, row2, col2) is False:
                    return False
                if self.dfs(row2, col2) is False:
                    return False
            if neighbor not in self.processed:
                row2, col2 = neighbor
                if self.process_edge(row, col, row2, col2) is False:
                    return False
        self.processed.add((row, col))
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = Sudoku(board)
        return s.dfs()

s = Solution()
mat = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(mat))

mat = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(mat))

mat = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
__import__('ptpython.repl', fromlist=('repl')).embed(globals(), locals(), vi_mode=False, history_filename=None)
pprint(mat)

