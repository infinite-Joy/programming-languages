from collections import defaultdict
from enum import Enum


class EdgeType(Enum):
    BACKEDGE = 0
    FRONTEDGE = 1
    CROSSEDGE = 2


class DAGGraph:

    def __init__(self, root=None, directed=None):
        self._graph = defaultdict(list)
        self._root = root
        self.directed = directed
        self.entry_time = {}
        self.exit_time = {}
        self.discovered = {}
        self.processed = {}
        self.parent = {self._root: None}
        self.topological_sorting = []

    def add_edge(self, u, *vs):
        if self._root is None:
            self._root = u
        self._graph[u].extend(vs)

    def finished(self):
        if len(self.discovered) == len(self._graph):
            return True

    def edge_classification(self, u, v):
        # the idea is that in a dag the entry times to nodes higher in the
        # execution tree will have entry times before the dags lower in the
        # tree. so if this is not matching that means that there is a ancestor
        # here.
        v_entry_time = self.entry_time.get(v, None)
        if v_entry_time:
            u_entry_time = self.entry_time.get(u, None)
            if u_entry_time:
                if v_entry_time < u_entry_time:
                    return EdgeType.BACKEDGE

    def process_vertex_early(self, vertex):
        print("process_vertex_early", vertex)

    def process_vertex_late(self, vertex):
        print("process_vertex_late", vertex)
        self.topological_sorting.append(vertex)

    def process_edge(self, u, v):
        print("processing edge {} -> {}".format(u, v))
        edge_type = self.edge_classification(u, v)
        if edge_type == EdgeType.BACKEDGE:
            raise ValueError("Not a dag")

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
print("valid DAG")
g = DAGGraph(0, directed=True)
g.add_edge(0, 1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4, 5)
g.add_edge(4, 6)
g.add_edge(5, 7)
g.add_edge(6, 7)
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
topological_sorting = [str(x) for x in reversed(g.topological_sorting)]
print("topological_sortin: {}".format(" -> ".join(topological_sorting)))

print("invalid DAG")
g = DAGGraph(0, directed=True)
g.add_edge(0, 1, 2)
g.add_edge(1, 3)
g.add_edge(2, 1)
g.add_edge(3, 4)
g.add_edge(4, 2)
g.dfs()
