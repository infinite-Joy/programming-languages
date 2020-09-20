"""
strange printer

thinking in terms of upper bound and lower bound.

once we have the upper bound and lower bound of the colors we will run them through the backtracking key

run a dfs on the graph

we will see if we can do the

this does not seem like a union find solution
"""



from collections import defaultdict
from enum import Enum
from typing import List
class EdgeClass(Enum):
    BACK = 0
    OTHER = 1
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        self.processed = set()
        self.directed = True
    def add_edge(self, u, v):
        self.graph[u].add(v)
    def edge_classification(self, u, v):
        if v in self.visited and v not in self.processed:
            return EdgeClass.BACK
        return EdgeClass.OTHER
    def dfs(self, vertex):
        self.visited.add(vertex)
        for nnode in self.graph[vertex]:
            if nnode not in self.visited:
                edge_class = self.edge_classification(vertex, nnode)
                if edge_class == EdgeClass.BACK:
                    return False
                if not self.dfs(nnode):
                    return False
            if nnode not in self.processed or self.directed:
                edge_class = self.edge_classification(vertex, nnode)
                if edge_class == EdgeClass.BACK:
                    return False
        self.processed.add(vertex)
        return True
    def topological_sort(self):
        self.visited = set()
        colors = list(self.graph.keys())
        for color in colors:
            if color not in self.visited:
                if not self.dfs(color):
                    return False
        return True

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = {} # colors -> (ub, lb)
        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[0])):
                color = targetGrid[row][col]
                if color not in colors:
                    colors[color] = [[row, col], [row, col]]
                colors[color][0][0] = min(colors[color][0][0], row)
                colors[color][0][1] = min(colors[color][0][1], col)
                colors[color][1][0] = max(colors[color][1][0], row)
                colors[color][1][1] = max(colors[color][1][1], col)
        print(colors)
        graph = Graph()
        for color, ((lbrow, lbcol), (ubrow, ubcol)) in colors.items():
            for row in range(lbrow, ubrow + 1):
                for col in range(lbcol, ubcol + 1):
                    cellcolor = targetGrid[row][col]
                    if cellcolor != color:
                        graph.add_edge(color, cellcolor)
        print(graph.graph)
        # we need to detect cycle now. if cycle exists then not possible
        # this is a topological sort example
        return graph.topological_sort()


targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
sol = Solution()
print(sol.isPrintable(targetGrid))

targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
sol = Solution()
print(sol.isPrintable(targetGrid))

targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
sol = Solution()
print(sol.isPrintable(targetGrid))

targetGrid = [[1,1,1],[3,1,3]]
sol = Solution()
print(sol.isPrintable(targetGrid))
