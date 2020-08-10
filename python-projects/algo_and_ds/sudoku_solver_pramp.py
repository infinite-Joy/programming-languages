"""

1. loop through the rows and cols
    loop throught the rows, loop through the col and the sub board and
    find the possible values

    for some row col comb. if the possible available value list is empty
        that means a solution is not possible.

1. dfs approach on all cells:
    pick one elem and check if there are no inconsitencies
2.

time complexity: O((n)**(n**2))
space complexity: O(1)

a sudoku board is np complete for an n x n board

"""
from pprint import pprint

class Sudoku:
    def __init__(self, board):
        self.board = board
        self.visited = {}

    def check_rows_cols(self, row, col):
        for rr in range(9):
            if row != rr or self.board[rr][col] != '.':
                yield self.board[rr][col]
        for cc in range(9):
            if col != cc or self.board[row][cc] != '.':
                yield self.board[row][cc]

    def check_subboard(self, row, col):
        rowstart = (row // 3) * 3
        rowend = rowstart + 3
        colstart = (col // 3) * 3
        colend = colstart + 3
        for rr in range(rowstart, rowend):
            for cc in range(colstart, colend):
                if col != cc and row != rr and self.board[rr][cc] != '.':
                    yield self.board[rr][cc]

    def possible_values(self, row, col):
        pvs = set(list(range(9)))
        pvs.difference_update(self.check_subboard(row, col))
        pvs.difference_update(self.check_subboard(row, col))
        return pvs

    def get_empty(self):
        all_empties = []
        for rr in range(9):
            for cc in range(9):
                if self.board[rr][cc] == '.':
                    all_empties.append((rr, cc))

    def sudoku_solve(self, row, col):
        for row, col in self.get_empty():
            pass


from itertools import combinations_with_replacement

def sudoku_solve(board):
    s = Sudoku(board)
    all_empties = s.get_empty()
    fr = all_empties[0][0]
    fc = all_empties[0][1]
    s.sudoku_solve(fr, fc)


################################################

# will be solving based mit solution
# https://www.youtube.com/watch?v=auK3PSZoidc

# global variable set to 0
BACKTRACKS = 0

def find_next_cell_to_fill(grid):
    """Find the next empty square to fill"""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '.':
                return row, col
    return None, None


def is_valid(grid, row, col, e):
    """This checks if the setting grid setting for e in row, col is valid"""
    # check in the rows
    row_ok = all([e != grid[row][cc] for cc in range(9)])
    if row_ok is False:
        return False

    # check in the column
    col_ok = all([e != grid[rr][col] for rr in range(9)])
    if col_ok is False:
        return False

    # check in the subgrid
    startrow = int(row//3) * 3
    startcol = int(col//3) * 3
    for rr in range(startrow, startrow+3):
        for cc in range(startcol,  startcol+3):
            if grid[rr][cc] == e:
                return False
    return True


def sudoku_solve_b(grid):
    global BACKTRACKS

    # find the next cell to fill
    row, col = find_next_cell_to_fill(grid)
    if row is None:
        return True # the whole grid is complete and nothing else needs to be done

    # try for different values
    for e in range(1, 10):
        e = str(e)
        if is_valid(grid, row, col, e):
            possible_values = True

            # the do logic
            grid[row][col] = e
            if sudoku_solve_b(grid):
                return True

            # undo the current cell for backtracking
            BACKTRACKS += 1
            if BACKTRACKS % 100 == 0:
                print(BACKTRACKS)
            grid[row][col] = '.'

    return False

#grid = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
#pprint(grid)
#print(sudoku_solve(grid))
#print(BACKTRACKS)
#
#BACKTRACKS = 0
#grid = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
#print(sudoku_solve(grid))
#print(BACKTRACKS)
#
#BACKTRACKS = 0
#grid = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
#print(sudoku_solve(grid))
#print(BACKTRACKS)


#################################

# to do this we will need just need to implement a basic material

def sudoku_solve(grid):
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    subgrid_set = [[set() for _ in range(3)] for _ in range(3)]

    for row in range(9):
        for col in range(9):
            val = grid[row][col]
            if val != '.':
                val = int(val)
                if val > 9 or val < 0:
                    return False

                # check the rows
                if val in row_set[row]:
                    return False
                else:
                    row_set[row].add(val)

                # check the cols
                if val in col_set[col]:
                    return False
                else:
                    col_set[col].add(val)

                # check the subgrid
                sgrow = row // 3
                sgcol = col // 3
                if val in subgrid_set[sgrow][sgcol]:
                    return False
                else:
                    subgrid_set[sgrow][sgcol].add(val)

    return sudoku_solve_b(grid)


BACKTRACKS = 0
grid = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
pprint(grid)
print(sudoku_solve(grid))

BACKTRACKS = 0
grid = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
pprint(grid)
print(sudoku_solve(grid))

BACKTRACKS = 0
grid = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
pprint(grid)
print(sudoku_solve(grid))
pprint(grid)
