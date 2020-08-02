"""
https://leetcode.com/problems/course-schedule/
find courses in  the graph
we can create a adjacency list
and then do a dfs
basically try to find the backedges
============================
"""

from collections import defaultdict
from enum import Enum


class EdgeClass(Enum):
    BACK = 0
    OTHER = 1


class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.discovered = {}
        self.processed = {}
        self.root = None
        self.directed = True
        self.cycle = False
    def add_edge(self, u, v):
        if self.root is None:
            self.root = u
        self.g[u].append(v)
    def is_back_edge(self, u, v):
        if self.discovered.get(v, False) and not self.processed.get(v, False):
            return True
    def dfs(self, v=None):
        #print(v, self.g[v], self.root, self.discovered, self.processed)
        if v is None:
            v = self.root
            self.discovered = {}
            self.processed = {}
        self.discovered[v] = True
        for child in self.g[v]:
            #__import__('pdb').set_trace()
            if child not in self.discovered:
                if self.is_back_edge(v, child) is True:
                    self.cycle = True
                self.dfs(child)
            elif child not in self.processed or self.directed is True:
                if self.is_back_edge(v, child) is True:
                    self.cycle = True
            else:
                pass
        self.processed[v] = True


def main(numCourses, prerequisites):
    graph = Graph()
    for u, v in prerequisites:
        graph.add_edge(u, v)
    # although I am doing another forloop there is an implicit memoisation here
    # as part of the visited graph. those nodes are not already discovered and
    # processed and hence will be processed again
    for i, _  in prerequisites:
        #print('source', i)
        graph.dfs(i)
        if graph.cycle:
            return False
    return True

print(main(2, [[1,0],[0,1]]))
print(main(2, [[1,0]]))
print(main(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
