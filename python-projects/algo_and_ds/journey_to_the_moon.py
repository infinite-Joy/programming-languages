"""
https://www.hackerrank.com/challenges/journey-to-the-moon/problem
using union find we define the roots of all the astros and then find the groupings of all the astros
answer = all combinations - ∑(combinations of all the groups)

"""

from functools import reduce
import operator as op


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.components = set([i for i in range(size)])
        self._id = [i for i in range(size)]
        self.sz = [1 for _ in range(size)]

    def find(self, p):
        root = p
        while root!=self._id[p]:
            root = self._id[p]
        while p!=root:
            next_p = self._id[p]
            self._id[p] = root
            p = next_p
        return root

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        if self.is_connected(p, q) is False:
            root1 = self.find(p)
            root2 = self.find(q)
            if self.sz[root1] < self.sz[root2]:
                self.sz[root2] += self.sz[root1]
                self._id[root1] = root2
                self.components.remove(root1)
            else:
                self.sz[root1] += self.sz[root2]
                self._id[root2] = root1
                self.components.remove(root2)


def ncr(n, r):
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n-r, -1), 1)
    den = reduce(op.mul, range(r, 0, -1), 1)
    return num // den


def main(N, edges):
    print("%"*10)
    g = UnionFind(N)
    print(g.sz, g.components, g._id)
    for v1, v2 in edges:
        g.union(v1, v2)
    print(g.sz, g.components, g._id)
    total_combinations = ncr(N, 2)
    for component in g.components:
        component_size = g.sz[component]
        if component_size > 1:
            total_combinations = total_combinations - ncr(component_size, 2)
    return total_combinations


#print(main(5, [[0, 1], [2, 3], [0, 4]]))
#print(main(4, [[0, 2]]))
print(main(10, [[0, 2], [1,8], [1,4], [2, 8], [2, 6], [3, 5], [6, 9]])) # expected 23
