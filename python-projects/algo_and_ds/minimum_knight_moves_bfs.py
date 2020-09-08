"""

minimum knight moves

going through a normal bfs

time complexity : O(target - source)2 or the square of the euclidian distance

"""
from collections import deque
class Solution:
    def next_move(self, x, y, visited):
        # upright, upleft, leftup, leftdown, downleft. downright, rightdown, rightup
        delta_xs = [1, -1, -2, -2, -1, 1, 2, 2]
        delta_ys = [2, 2, 1, -1, -2, -2, -1, 1]
        for delta_x, delta_y in zip(delta_xs, delta_ys):
            new_x = x + delta_x
            new_y = y + delta_y
            if (new_x, new_y) not in visited:
                yield new_x, new_y
    def bfs(self, x, y):
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        while queue:
            currx, curry, moves = queue.popleft()
            if currx == x and curry == y:
                return moves
            for next_move_x, next_move_y in self.next_move(currx, curry, visited):
                queue.append((next_move_x, next_move_y, moves + 1))
                visited.append((next_move_x, next_move_y))
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.bfs(x, y)

