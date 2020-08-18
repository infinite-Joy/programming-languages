# https://www.hackerrank.com/test/61sq9qfa63d/questions/3j99sc3rf3p

# the simple approach is that do a dfs and find the edges that are connecting
# the machines.
# sort those edges up
# and then find the sum of the edges - 1
# complexity is O(V + mlogm) where m is the number of machines

from collections import defaultdict


class Graph:
    """
    Graph to have the nodes and then perform graph operations"""
    def __init__(self):
        self.g = defaultdict(list)
        self.bridges = set()
        self.visited = set()
    def add_edge(self, u, v, cost):
        """add the edge from u to v with cost"""
        self.g[u].append((v, cost))
        self.g[v].append((u, cost))
    def dfs(self, node, machines):
        """Do an inorder traversal of the graph"""
        self.visited.add(node)
        for nnode, cost in self.g[node]:
            if nnode not in self.visited:

                # add the bridge with the cost
                if node in machines and nnode in machines:
                    if (node, nnode) not in self.bridges or (nnode, node) not in self.bridges:
                        self.bridges.add((node, nnode, cost))
                elif node in machines:
                    self.bridges.add((node, nnode, cost))
                elif nnode in machines:
                    self.bridges.add((nnode, node, cost))

                self.dfs(nnode, machines)


def minTime(roads, machines):
    # edge case there is only one node and that is probably the machine
    if len(roads) == 1:
        return 0

    # now going ahead withe meain code.
    machines = set(machines)
    g = Graph()
    for u, v, cost in roads:
        g.add_edge(u,v,cost)

    starting_node = next(iter(machines))
    g.dfs(starting_node, machines)

    machines_edges = list(g.bridges)
    machines_edges_cost = [x[2] for x in machines_edges]
    machines_edges_cost.sort()
    return sum(machines_edges_cost[:-1])

graph = [[2, 1, 8], [1, 0, 5], [2, 4, 5], [1, 3, 4]]
machines = [2,4,0]
print(minTime(graph, machines))
