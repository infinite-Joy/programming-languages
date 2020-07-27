"""
this looks to be a simple problem of DFS with backtracking and pruning.

using a BFS solution for this, hence to find the starting position we can the O(nm)

"""

from collections import deque


class Cell:
    WALL = #
    PLAYER = S
    BOX = B
    TARGET = T
class Game:
    def __init__(self, grid):
        self.start = grid
        self.grid = grid
        self.visited = {}
    def understand_state(self, grid):
        playerrow, playercol, boxrow, boxcol, targetrow, targetcol = None, None, None, None, None, None
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == Cell.TARGET:
                    targetrow, targetcol = row, col
                if grid[row][col] == Cell.PLAYER:
                    playerrow, playercol = row, col
                if grid[row][col] == Cell.BOX:
                    boxrow, boxcol = row, col
        return playerrow, playercol, boxrow, boxcol, targetrow, targetcol
    def next_player_state(self, playerrow, playercol. boxrow, boxcol):
        if playerrow+1<len(grid) and grid[playerrow+1][playercol] not in (Cell.WALL, Cell.BOX):
        yield 0, playerrow+1, playercol, boxrow, boxcol
    if playerrow-1>0 and grid[playerrow-1][playercol] not in (Cell.WALL, Cell.BOX):
        yield 0, playerrow-1, playercol, boxrow, boxcol
    if playercol-1>0 and grid[playerrow][playercol-1] not in (Cell.WALL, Cell.BOX):
        yield 0, playerrow, playercol-1, boxrow, boxcol
    if playercol+1<len(grid[0]) and grid[playerrow][playercol+1] not in (Cell.WALL, Cell.BOX):
        yield 0, playerrow, playercol+1, boxrow, boxcol
    def next_states(self, playerrow, playercol, boxrow, boxcol, grid):
        if (     # if player not adjacent to box
(boxrow-1, boxcol) != (playerrow, playercol) or
(boxrow, boxcol-1) != (playerrow, playercol) or
(boxrow+1, boxcol) != (playerrow, playercol) or
(boxrow, boxcol+1) != (playerrow, playercol)
):
    yield from self.next_player_state(playerrow, playercol, boxrow, boxcol)
else:
    # there can be only 2 states, player not beside box or player beside box
    if (boxrow-1, boxcol) == (playerrow, playercol):     # player above box
        if boxrow+1<len(grid) and grid[boxrow+1][boxcol] != Cell.WALL: # go down
            # player will go to wherever the current box is. this means pushing
return [(1, boxrow, boxcol, boxrow+1, boxcol)]
else:
    # player is adjacent to the box but cannot move the box
    yield from self.next_player_state(playerrow, playercol, boxrow, boxcol)
            if (boxrow+1, boxcol) == (playerrow, playercol):     # player below box
        if boxrow-1>0 and grid[boxrow-1][boxcol] != Cell.WALL: # go up
yield (1, boxrow, boxcol, boxrow-1, boxcol)
else:
    yield from self.next_player_state(playerrow, playercol, boxrow, boxcol)
            if (boxrow, boxcol-1) == (playerrow, playercol):     # player left of box
        if boxcol+1<len(grid[0]) and grid[boxrow][boxcol+1] != Cell.WALL: # go right
return [(1, boxrow, boxcol, boxrow, boxcol+1)]
else:
    yield from self.next_player_state(playerrow, playercol, boxrow, boxcol)
            if (boxrow, boxcol+1) == (playerrow, playercol):     # player right of box
        if boxcol-1>0 and grid[boxrow][boxcol-1] != Cell.WALL: # go left
return [(1, boxrow, boxcol, boxrow, boxcol)]
else:
    yield from self.next_player_state(playerrow, playercol, boxrow, boxcol)
    def bfs(self, playerrow, playercol, boxrow, boxcol, targetrow, targetcol):
        # i want the shortest route to target, hence bfs
        queue = deque([(playerrow, playercol, boxrow, boxcol)])
        moves = 0
        visited = set([(playerrow, playercol, boxrow, boxcol)])
        while queue:
            c, *curr_state = queue.popleft()
            playerrow, playercol, boxrow, boxcol = curr_state
            if boxrow == targetrow and boxcol == targetcol:
                return moves
            for nextstate in self.next_states(*curr_state):
                if state not in visited:
                    queue.append(state)
                    visited.add(state)
            moves+=c

        # there is no path from the starting conf of player to target
return False
    def play(self):
        playerrow, playercol, boxrow, boxcol, targetrow, targetcol = self.understand_state(self.grid)
        moves = self.bfs(playerrow, playercol, boxrow, boxcol, targetrow, targetcol)
        if moves:
            return moves
        else:
            -1
