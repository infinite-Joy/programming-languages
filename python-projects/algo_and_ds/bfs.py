from collections import defaultdict
from collections import deque


class Graph:

    def __init__(self, root, directed=None):
        # we will create an adjaceency list for the graph
        self._graph = defaultdict(list)
        self._root = root
        self._number_of_vertices = 0
        self.parents = None
        self.directed = directed

    def add_edge(self, u, *vertices):
        if self._root is None:
            self._root = u
        for v in vertices:
            self._graph[u].append(v)
            self._number_of_vertices += 1

    def process_vertex(self, curr_node, s, parents):
        if curr_node == s:
            self.parents = parents
            return s

    def bfs(self, s):
        queue = deque([self._root])
        processed = defaultdict(bool)
        visited = {self._root: True}
        parent = {self._root: None}
        while queue:
            v = queue.popleft()
            self.process_vertex_early(v)
            yield v
            if v == s:
                return
            processed[v] = True
            for child in self._graph[v]:
                if child not in processed or self.directed is True:
                    self.process_edge(v, child)
                if child not in visited:
                    queue.append(child)
                    visited[child] = True
                    parent[child] = v

            self.process_vertex_late(v)

    def process_vertex_early(self, v):
        print("process_vertex_early", v)

    def process_edge(self, u, v):
        print("process vertex {} -> {}".format(u, v))

    def process_vertex_late(self, v):
        print("process_vertex_late", v)

    def bfs_find_path(self, start, end):
        queue = deque([start])
        level = {start: 0}
        parent = {start: None}
        while queue:
            v = queue.popleft()
            if v == end:
                break
            for child in self._graph[v]:
                if child not in level:
                    queue.append(child)
                    level[child] = level[v] + 1
                    parent[child] = v
        shortest_path = []
        shortest_path.append(end)
        curr_node = end
        while parent[curr_node]:
            curr_node = parent[curr_node]
            shortest_path.append(curr_node)
        return shortest_path


    def find_path(self, start, end):
        if start == end or end is None:
            yield start
        else:
            yield self.find_path(start, self.parents[end])




print('testing bfs')
# Driver code
g = Graph(0)
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

print('testing bfs of graphs')
# Driver code
g = Graph(0)
g.add_edge(0, 1, 2)
g.add_edge(1, 0, 2, 3)
g.add_edge(2, 0, 1, 4)
g.add_edge(3, 1, 4, 5)
g.add_edge(4, 2, 3, 6)
g.add_edge(5, 3, 6)
g.add_edge(6, 4, 5)
print(g._graph)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 0)")
visited = g.bfs(6)
print(" - ".join([str(x) for x in visited]))

shortest_path = g.bfs_find_path(1, 6)
print(" -> ".join(reversed(list(map(lambda x: str(x), shortest_path)))))
