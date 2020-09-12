"""

evaluate division

can be done using dfs

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

so basically we will be creating the nodes and then whenever

ideally i am thinking a bfs would make more sense here as we should be looking for the shortest path

but that should be ok.

create a graph from then andn then implement dfs on it.

"""

from collections import defaultdict
from typing import List
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, 1./w))
    def dfs(self, vertex, end, visited, res):
        if vertex == end:
            return res
        visited.add(vertex)
        for nvertex, weight in self.graph[vertex]:
            if nvertex not in visited:
                output = self.dfs(nvertex, end, visited, res * weight)
                if output:
                    return output

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph()
        for (u, v), w in zip(equations, values):
            graph.add_edge(u, v, w)
        sol = []
        for start, end in queries:
            visited = set()
            if start in graph.graph:
                out = graph.dfs(start, end, visited, 1.0)
            else:
                out = None
            if out:
                sol.append(out)
            else:
                sol.append(-1.0)
        return sol

# test cases
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
sol = Solution()
print(sol.calcEquation(equations, values, queries))

