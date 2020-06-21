from collections import defaultdict
from collections import deque


class Graph:

    def __init__(self, root):
        # we will create an adjaceency list for the graph
        self._graph = defaultdict(list)
        self._root = root
        self._number_of_vertices = 0
        self.parents = None

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

    #def bfs(self, s):
    #    # recursion is not a good choice for the breadth first search
    #    queue = deque([self._root])
    #    processed = defaultdict(bool)
    #    discovered = defaultdict(bool)
    #    parent = defaultdict(None)
    #    discovered[self._root] = True
    #    while queue:
    #        curr_node = queue.popleft()
    #        output = self.process_vertex(curr_node, s, parent)
    #        if output:
    #            yield output
    #            return
    #        yield curr_node
    #        if parent.get(curr_node):
    #            processed[str(parent[curr_node])+str(curr_node)] = True
    #        else:
    #            processed[str(curr_node)] = True
    #        for child in self._graph[curr_node]:
    #            if processed[str(curr_node)+str(child)] is False:
    #                output = self.process_vertex(curr_node, s, parent)
    #                if output:
    #                    yield output
    #                    return
    #            if discovered[child] is False:
    #                queue.append(child)
    #                discovered[child] = True
    #                parent[child] = curr_node

    def bfs(self, s):
        queue = deque([self._root])
        visited = {self._root: True}
        while queue:
            v = queue.popleft()
            yield v
            if v == s:
                return
            for child in self._graph[v]:
                if child not in visited:
                    queue.append(child)
                    visited[child] = True

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
