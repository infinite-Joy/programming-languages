from collections import defaultdict


class Graph:

    def __init__(self, root=None, directed=None):
        self._graph = defaultdict(list)
        self._root = root
        self.directed = directed
        self.entry_time = {}
        self.exit_time = {}
        self.discovered = {}
        self.processed = {}
        self.parent = {}

    def add_edge(self, u, *vs):
        if self._root is None:
            self._root = u
        self._graph[u].extend(vs)

    def finished(self):
        if len(self.discovered) == len(self._graph):
            return True

    def process_vertex_early(self, vertex):
        print("process_vertex_early", vertex)

    def process_vertex_late(self, vertex):
        print("process_vertex_late", vertex)

    def process_edge(self, u, v):
        print("processing edge {} -> {}".format(u, v))

    def dfs(self, v=None, time=None):
        if v is None:
            v = self._root
        if time is None:
            time = 1
        #if self.finished():
        #    return
        self.discovered[v] = True
        time = time + 1
        self.entry_time[v] = time;
        self.process_vertex_early(v)
        for child in self._graph[v]:
            if child not in self.discovered:
                self.parent[child] = v
                self.process_edge(v, child)
                self.dfs(child, time)
            elif child not in self.processed or self.directed:
                self.process_edge(v, child)
            else:
                pass
            #if self.finished():
            #    return
        self.process_vertex_late(v)

        time += 1
        self.exit_time[v] = time

        self.processed[v] = True

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
print(g._root)
print(g.directed)

print ("Following is Depth First Traversal"
                  " (starting from vertex 0)")
g.dfs()
print("entrytmie", g.entry_time)
print("exit time", g.exit_time)
print("discovered", g.discovered)
print("processed", g.processed)
print("parent", g.parent)
print()
