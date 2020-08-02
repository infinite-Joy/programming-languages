"""
https://leetcode.com/problems/surrounded-regions/
what needs to be done is that basically  find the two  groups of o’s
we basically classify them into edge o and non edge o and then union all of them
whichever group is non edge we flip them up
once i have the union find.
union all the xs
union all the edge o’s
now recursively for inner and inner o’s check if they are connected to an then connect them
    or maybe a priority queue of o’s can be done
once all the o’s are done
then get the o’s which are not connected and flip them
============================================================
"""
class UnionFind:
    def __init__(self, size):
        self._size = size
        self._comp_sizes = [i for i in range(size)]
        self._groups = [1 for 1 in range(size)]
        self._num_comps = size
        self.root_side_o = None

    def _find(self, p, groups=None):
        if groups is None:
            groups = self._groups
        if groups[p] == p:
            return p
        groups[p] = self._find(groups[p], groups)
        return groups[p]
    def union(self, p, q):
        root1 = self._find(p)
        root2 = self._find(q)
        if root1 == root2:
            return
        # merge the smaller one to the larger one
        if self._comp_sizes[root1] >= self._comp_sizes[root2]:
            self._comp_sizes[root1] += self._comp_sizes[root2]
            self._groups[root2] = root1
        else:
            self._comp_sizes[root2] += self._comp_sizes[root1]
            self._groups[root1] = root2
        self._num_comps -= 1
    def union_side_o(self, p):
        if self.root_side_o is None:
            self.root_side_o = p
        else:
            self.union(self.root_side_o, p)
    def get_index(i, j, board):
        return len(board)*i+j

    def is_connected_to_edge(self, p):
        if self._find(p) == self._find(self.root_side_o):
            return True


class Solution:
    def traverse_spiral(self, board, topleft, downright, actualtopleft=(0,0), actualdownright=(len(board)-1, len(board[0])-1), uf):
        # top left -> top right
        for i in range(topupper[1], downright[1]):
            if board[topleft[0]][i] == ‘o’:
            if i == actualtopleft[0]:
                self.union_side_o(get_index(topleft[0], i))
            else:
                if board[topleft[0]-1][i] == ‘o’:
                    p = get_index(topleft[0], i))
                    q = get_index(topleft[0]-1, i))
                    self.union(p, q)
        topleft[1] += 1
        # topright -> downright
        for i in range(topleft[0], downright[0]):
            if board[i][downright[1]] == ‘o’:
            if i == actualdownright[1] and
                self.union_side_o(get_index(i, downright[1]))
            else:
                if board[i][downright[1]+1] == ‘o’:
                    p = get_index(i, downright[1]))
                    q = get_index(i, downright[1]+1))
                    self.union(p, q)
        downright[1] -= 1
        # bottom right -> bottom left
        for i in range(downright[1], topleft[1], -1):
            if board[downright[0]][i] == ‘o’:
            if i == actualdownright[0]:
                self.union_side_o(get_index(downright[0], i))
            else:
                if board[downright[0]+1][i] == ‘o’:
                    p = get_index(downright[0], i))
                    q = get_index(downright[0]+1, i))
                    self.union(p, q)
        downright[0] -= 1
        # downleft -> topleft
        for i in range(downright[0], topleft[0], -1):
            if board[i][topleft[0]] == ‘o’:
            if i == actualtopleft[1]:
                self.union_side_o(get_index(i, topleft[1]))
            else:
                if board[i][topleft[0]-1] == ‘o’:
                    p = get_index(i,topleft[0]))
                    q = get_index(i, topleft[0]-1))
                    self.union(p, q)
    topleft[0] += 1
        self.traverse_spiral(board, topleft, downright, actualtopleft=(0,0), actualdownright=(len(board)-1, len(board[0])-1), uf)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        uf = UnionFind(len(board) * len(board[0]))
        traverse_spiral(
            board,
            topleft=[0,0], downright=[len(board)-1,
            len(board[0])-1], actualtopleft=(0,0),
            actualdownright=(len(board)-1, len(board[0])-1),
            uf)
        # once i have grouped in the board then i can traverse the board and change to x
        # wherever not connected to the side
        for i in range(len(board)):
            for j in range(len(board[0])):
                uf_index = get_index(i, j)
                if not self.is_connected_to_edge(uf_index):
                    board[i, j] = ‘x’


