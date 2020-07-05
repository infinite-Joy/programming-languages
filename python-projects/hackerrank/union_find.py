# this is the union find data structure
# also known as disjoint set

# references
# https://iq.opengenus.org/kruskal-minimum-spanning-tree-algorithm/
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
#

class UnionFind:

    def __init__(self):
        # number of elements in this union find
        size = 0

        # used to track the sizes of each of the components
        sz = []

        # pointer[i] points to the parent of i, if id[i] == i then i is the root
        # node
        pointer = []

        # tracks the number of components in the union find
        num_components = 0



    @classmethod
    def create(cls, size):
        if size == 0:
            raise TypeError("union find with size 0 is not allowed")
        cls.size = size
        cls.num_components = size
        cls.sz = [1 for _ in range(size)]
        cls.pointer = [i for i in range(size)]

    def find(self, p):
        """
        Find which component/set 'p' belongs to
        """
        # find the root of the component set
        root = p
        while root!=self.pointer[p]:
            root = self.pointer[p]

        # compress the path leading to the root
        # doing this operation is called path compression
        # and gives us amortized constant time operation
        while p!=root:
            next_p = self.pointer[p]
            self.pointer[p] = root
            p = next_p

        return root

    def connected(self, p, q):
        """
        Return whether or not p and q are in the same component/set
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Unify the components belonging to p and q
        """
        root1 = self.find(p)
        root2 = self.find(q)

        # if p and q  belong to the same group
        if root1 == root2:
            return

        # merge two component sets together
        # merge smaller component set to the larger one
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.pointer[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.pointer[root2] = root1

        # since the roots found are different we know  that the number of
        # components  has decreased by 1
        self.num_components -= 1


class Graph(UnionFind):
    def __init__(self, vertices):
        # this is the number of vertices
        self.V = vertices
        self.graph = []
        self.create(vertices)

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def krushkal(self):
        result = []
        i, e = 0, 0

        # sort edge by ascending edge  weight
        self.graph = sorted(self.graph, key=lambda x: x[2])
        print('graph: ', self.graph)

        # only |v|-1 subset required for the MST
        while e < self.V-1:
            print('pointer: ', self.pointer, 'components: ', self.sz)
            try:
                u, v, w = self.graph[i]
                i += 1
                x = self.find(u)
                y = self.find(v)
                if x != y: # cycle means that the edges belong to the same group
                    e += 1
                    result.append((u, v, w))
                    self.union(x, y)
            except KeyError: # no more edges left
                # making e a large value to break out of the loop
                e = self.V ** 2.71828

        print("Constructed MST :")
        print("Vertex A    Vertex B  Weight")
        for u, v, weight in result:
            print ("    %d          %d        %d" % (u,v,weight))

eegde = 6
g = Graph(eegde)
print("For each edge input (Source vertex , Destination vertex , Weight of the edge ) :")
vertices = "abcdef"
edges = {k: v for k, v in zip(vertices, range(len(vertices)))}
print(edges)
edges1 = {('a', 'b'): 4, ('a', 'f'): 2, ('b', 'c'): 6, ('b', 'f'): 5, ('c', 'd'): 3, ('c', 'f'): 1, ('d', 'e'): 2, ('e', 'f'): 4}
print(edges1)
for x, y in edges1.items():
    u, v, w = edges[x[0]], edges[x[1]], y
    g.add_edge(u, v, w)
g.krushkal()
