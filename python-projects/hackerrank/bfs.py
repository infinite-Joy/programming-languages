from collections import defaultdict
from collections import deque


class Graph:

    def __init__(self):
        self._graph = defaultdict(list)
        self._root = None

    def add_edge(self, u, v):
        if self._root is None:
            self._root = u
        self._graph[u].append(v)

    def bfs(self, s):
        # recursion is not a good choice for the breadth first search
        queue = deque([self._root])
        while queue:
            curr_node = queue.popleft()
            if curr_node == s:
                yield s
                return
            yield curr_node
            for child in self._graph[curr_node]:
                queue.append(child)



print('testing bfs')
# Driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(2, 7)
print(g._graph)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
visited = g.bfs(6)
print(" - ".join([str(x) for x in visited]))
