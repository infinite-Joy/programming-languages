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
        if self.discovered.get(v, False) is True and self.processed.get(v, False) is False:
            return True
    def dfs(self, v=None):
        print(v, self.g[v], self.root, self.discovered, self.processed)
        if v is None:
            v = self.root
            self.discovered = {}
            self.processed = {}
        self.discovered[v] = True
        for child in self.g[v]:
            __import__('pdb').set_trace()
            if child not in self.discovered:
                self.discovered[child] = True
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
    graph.dfs()
    return not graph.cycle

#print(main(2, [[1,0],[0,1]]))
print(main(2, [[1,0]]))
