"""

Given a function KNOWS(A,B), which returns 1 if A knows B (and not necessarily the other way around) and 0 if A does not know B.

A Celebrity is one who does not know anyone,
and one who is known by everybody.

For a list of N people, find all celebrities in linear time.

basically what i can do is that make an indegree hashmap

and then do a dfs and then update the indegree whenever we get something

finally whenever we get something that indegree

"""

def knows(a, b):
    # logic for telling if a knows b
    if b in (5, 10, 15):
        return 1
    return 0

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.directed = directed
        self.visited = set()
        self.processed = set()
        self.indegree = defaultdict(int)
        self.directed = True
        self.edges = set()
    def add_edge(self, u, v):
        # this is a directed graph only
        self.graph[u].append(v)
        self.edges.add(u)
        self.edges.add(v)
    @property
    def edgecount(self):
        return len(self.edges)
    def dfs(self, v):
        self.visited.add(v)
        for child in self.graph[v]:
            if child not in self.visited:
                self.indegree[child] += 1
                yield from self.dfs(child)
            if child not in self.processed or self.directed:
                self.indegree[child] += 1
        if self.indegree[v] >= self.edgecount - 1:
            yield v
        self.processed.add(v)
