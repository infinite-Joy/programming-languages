from pprint import pprint
from collections import deque


class Graph:
    def __init__(self, binaryMatrix):
        self.visited = set()
        self.binaryMatrix = binaryMatrix

    def check_adjoining_areas(self, row, col):
        if self.binaryMatrix[row][col] == 1:
            if (col-1)>=0 and self.binaryMatrix[row][col-1] == 1:
                yield row, col-1

            # check down
            if row + 1 < len(self.binaryMatrix) and self.binaryMatrix[row+1][col] == 1:
                yield row+1, col

            # check right
            if col + 1 < len(self.binaryMatrix[0]) and self.binaryMatrix[row][col+1] == 1:
                yield row, col+1

            # check top
            if row - 1 >= 0 and self.binaryMatrix[row-1][col] == 1:
                yield row-1, col

    def bfs(self, startrow, startcol):
        print(startrow, startcol, self.visited)
        queue = deque([tuple([startrow, startcol, 0])])
        self.visited.add((startrow, startcol))

        while queue:
            noderow, nodecol, level = queue.popleft()
            print('inside queue', startrow, startcol, noderow, nodecol, self.visited)
            # check in the adjoining areas
            for adj_row, adj_col in self.check_adjoining_areas(noderow, nodecol):
                if (adj_row, adj_col) not in self.visited:
                    queue.append(tuple([adj_row, adj_col, level+1]))
                    self.visited.add((adj_row, adj_col))


def get_number_of_islands(binaryMatrix):

    # edge case there is only one element
    if len(binaryMatrix) == 1 and len(binaryMatrix[0]) == 1:
        if binaryMatrix[0][0] == 1:
            return 1
        else:
            return 0


    # main algo
    g = Graph(binaryMatrix)
    num_islands = 0
    for row in range(len(binaryMatrix)):
        for col in range(len(binaryMatrix[0])):
            if (row, col) not in g.visited and binaryMatrix[row][col]==1:
                g.bfs(row, col)
                num_islands += 1

    return num_islands


binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

binaryMatrix = [ [ 1, 0, 1, 0] ]
binaryMatrix = [ [ 1, 0, 1, 0 ],
                    [ 0, 1, 1, 1 ],
                    [ 0, 0, 1, 0 ] ]
print('binaryMatrix')
pprint(binaryMatrix)

print(get_number_of_islands(binaryMatrix))










#Undirected graph traversal
"""
This seems to me a union find

space complexity: O(n)
time complexity: O(n*m * log(n*m))

                        A           B
binaryMatrix = [ [0,    1,    0,    1,    0],
                              B     B     E
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]


mat

0,1


backtracking:

scan through the matrix and create a graph with edges between the 1 and 1

visited = set

counter

while i in all nodes and i not in visited:
  count += 1
  do a dfs: add to visited

return count

complexity: O(n*m+e)
space: O(N+E)


"""
