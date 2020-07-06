"""
https://www.hackerrank.com/challenges/bfsshortreach/problem
implement the bfs function
"""

from collections import defaultdict, deque
class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.V = n
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self, start):
        root = start
        queue = deque([root])
        visited = {}
        parent = {}
        while queue:
            node = queue.popleft()
            visited[node] = True
            for child in self.graph[node]:
                if child not in visited:
                    queue.append(child)
                    parent[child] = node
        return parent

    def get_paths(self, parents, start, end, paths=None):
        if paths is None:
            paths = []
        if start == end:
            return paths
        else:
            parent = parents[end]
            paths.append(parent)
            return self.get_paths(parents, start, parent, paths)

    def get_distances(self, start, parents, vertices):
        solution = []
        for i in range(1, vertices+1):
            if i != start:
                if i in parents:
                    solution.append(6*len(self.get_paths(parents, start, i)))
                else:
                    solution.append(-1)
        return solution


def main(n,m,edges,s):
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)
    parents = g.bfs(s)
    print(parents)
    return g.get_distances(s, parents, n)

print(main(4, 2, [[1, 2], [1, 3]], 1))


