"""
design tic tac toe

https://leetcode.com/problems/design-tic-tac-toe/

leetcode 348

"""

# using a 2 layer set and hashmap architecture
# the move is O(1)

from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.player = [
            {'d':set(), 'xd': set(), 'r': defaultdict(int), 'c': defaultdict(int)},
            {'d':set(), 'xd': set(),  'r': defaultdict(int), 'c': defaultdict(int)}
        ]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        player_values = self.player[player - 1]

        # if this is a diagonal element, check if the diagonal elements are
        # filled now
        if row == col:
            player_values['d'].add(row)
            if len(player_values['d']) == self.n:
                return player

        # checking for the cross diagonal elements
        if row + col == self.n - 1:
            player_values['xd'].add(row)
            if len(player_values['xd']) == self.n:
                return player

        # maybe this is part of th row elements or col elements
        player_values['r'][row] += 1
        player_values['c'][col] += 1

        if player_values['r'][row] == self.n or player_values['c'][col] == self.n:
            print(row, col, player)
            print(self.player)
            return player

        print(row, col, player)
        print(self.player)

        return 0 # no one wins


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# test code
toe = TicTacToe(3)
print(toe.move(0, 0, 1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
print(toe.move(1, 1, 2))
print(toe.move(2, 0, 1))
print(toe.move(1, 0, 2))
print(toe.move(2, 1, 1))

print('#################')

["TicTacToe","move","move","move"]
vals = [[0,1,1],[1,1,2],[1,0,1]]
toe = TicTacToe(2)
for v in vals:
    print(toe.move(*v))

