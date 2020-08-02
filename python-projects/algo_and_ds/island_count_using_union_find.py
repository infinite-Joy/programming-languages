from pprint import pprint

class UnionFind:
    def __init__(self, mat):
        self.len_i = len(mat[0])

        # to whom does this group belong to
        self.group = [i for i in range(len(mat)*len(mat[0]))]

        # the size of the groups of the individual elements
        self.components = [1 for i in range(len(mat)*len(mat[0]))]

        # group together the zeros
        initial_zero = None
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    if initial_zero is None:
                        initial_zero = self.len_i*i+j
                    else:
                        #print(i, j, self.len_i*i+j)
                        self.group[self.len_i*i+j] = initial_zero
                        self.components[initial_zero] += 1

        # set groups count to non zeros
        self.num_groups = sum([True if g!=initial_zero else False for g in self.group])

        print('group', self.group)
        print('components', self.components)
        print('num_group', self.num_groups)

    def find(self, groups, i):
        # i have reached the root node
        if groups[i] == i:
            return i

        # path compression
        groups[i] = self.find(groups, groups[i])

        return groups[i]

    def union(self, p, q):
            p = self.len_i*p[0] + p[1]
            q = self.len_i*q[0] + q[1]

            root1 = self.find(self.group, p)
            root2 = self.find(self.group, q)

            if root1 == root2:
                return

            if self.components[root1] <= self.components[root2]:
                self.group[root2] = self.group[root1]
                self.components[root2] += self.components[root1]
            else:
                self.group[root1] = self.group[root2]
                self.components[root1] += self.components[root2]

            self.num_groups -= 1



def get_number_of_islands(binaryMatrix):

    # edge case there is only one element
    if len(binaryMatrix) == 1 and len(binaryMatrix[0]) == 1:
        if binaryMatrix[0][0] == 1:
            return 1
        else:
            return 0


    # main algo
    uf = UnionFind(binaryMatrix)

    for i in range(len(binaryMatrix)):
        for j in range(len(binaryMatrix[0])):
            if binaryMatrix[i][j] == 1:
                print(i, j)
                # check left
                if j-1>=0 and binaryMatrix[i][j-1] == 1:
                    uf.union((i,j), (i, j-1))
                # check down
                if i + 1 < len(binaryMatrix) and binaryMatrix[i+1][j] == 1:
                    uf.union((i,j), (i+1, j))
                # check right
                if j + 1 < len(binaryMatrix[0]) and binaryMatrix[i][j+1] == 1:
                    uf.union((i,j), (i, j+1))

                # check top
                if i - 1 >= 0 and binaryMatrix[i-1][j] == 1:
                    uf.union((i,j), (i-1, j))

                #__import__('pdb').set_trace()

                print(uf.group, uf.components, uf.num_groups)

    return uf.num_groups


#binaryMatrix = [ [0,    1,    0,    1,    0],
#                         [0,    0,    1,    1,    1],
#                         [1,    0,    0,    1,    0],
#                         [0,    1,    1,    0,    0],
#                         [1,    0,    1,    0,    1] ]

binaryMatrix = [[1,0,1,0]]
binaryMatrix = [
    [1,0,1,0],
    [0,1,1,1],
    [0,0,1,0]
]
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
