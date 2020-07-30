"""
so basically to give the list all the courses in the correct order
this is a perfect topological sorting question
for all nodes:
    if nodes not already visited
        do dfs starting from the node
in this way we cover all the nodes
time complexity: O(V+E)
space complexity: O(V+E)
===================================
"""
from enum import Enum
from collections import OrderedDict


class Edge(Enum):
    BACK = 0
    OTHER = 1
class Graph:
    def __init__(self, size):
        self.size = size
        self.visited = set()
        self.processed = set()
        self.parent = OrderedDict()
        self.graph = None
        self.sorted = []
    def create_graph(self, deps):
        graph = {k: [] for k in range(self.size)}
        for cour1, cour2 in deps:
            graph[cour2].append(cour1)
        self.graph = graph
    def edge_classification(self, u, v):
        if v in self.visited and v not in self.processed:
            return Edge.BACK
        else:
            return Edge.OTHER
    def process_vertex_late(self, v):
        self.sorted.append(v)
    def dfs(self, source):
        #__import__('pdb').set_trace()
        self.visited.add(source)
        for child in self.graph[source]:
            if child not in self.visited:
                if self.edge_classification(source, child) == Edge.BACK:
                    return False
                self.visited.add(child)
                self.parent[child] = source
                if self.dfs(child) is False:
                    return False
            if child not in self.processed:
                if self.edge_classification(source, child) == Edge.BACK:
                    return False
        self.process_vertex_late(source)
        self.processed.add(source)
        return True
    def get_topological_sort(self):
        for v in range(self.size):
            if v not in self.visited:
                if self.dfs(v) is False:
                    return []
        return self.sorted[::-1]
def main(size, pairs):
    if pairs == []:
        return [i for i in range(size)]
    g = Graph(size)
    g.create_graph(pairs)
    return g.get_topological_sort()

#size = 2
#pairs = [[1,0]]
#print(main(2, pairs))
#
#size = 4
#pairs = [[1,0],[2,0],[3,1],[3,2]]
#print(main(size, pairs))

size = 3
pairs = [[1,0]]
print(main(size, pairs))
