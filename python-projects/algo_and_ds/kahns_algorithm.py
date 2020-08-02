from collections import deque, defaultdict


class DAGGraph:
    def __init__(self, size):
        self.g = defaultdict(list)
        self.indegree = [0 for i in range(size)]
        self.size = size
        self.cycle = False

    def add_edge(self, u, *vs):
        for v in vs:
            self.indegree[v] += 1
        self.g[u].extend(vs)

    def kahns_topological_sort(self):
        queue = deque([i for i, elem in enumerate(self.indegree) if elem==0])
        count = 0
        while queue:
            node = queue.popleft()
            for neighbor in self.g[node]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
            count += 1
            yield node

        # check for cycle
        if count == len(self.g):
            self.cycle = False
        else:
            self.cycle = True


# Driver code
print("valid DAG")
g = DAGGraph(8)
g.add_edge(0, 1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4, 5)
g.add_edge(4, 6)
g.add_edge(5, 7)
g.add_edge(6, 7)
print(g.g)

top_sort = [x for x in g.kahns_topological_sort()]
print('top_sort', top_sort)
print('cycle', g.cycle)

print("invalid DAG")
g = DAGGraph(5)
g.add_edge(0, 1, 2)
g.add_edge(1, 3)
g.add_edge(2, 1)
g.add_edge(3, 4)
g.add_edge(4, 2)
top_sort = [x for x in g.kahns_topological_sort()]
print('top_sort', top_sort)
print('cycle', g.cycle)
