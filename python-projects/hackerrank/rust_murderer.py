#https://www.hackerrank.com/challenges/rust-murderer/problem

from collections import defaultdict, deque
import itertools
from functools import reduce

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, *v):
        self.graph[u].extend(v)
    def bfs(self, s, e):
        queue = deque([s])
        parent = {s:None}
        discovered = {}
        while queue:
            v = queue.popleft()
            discovered[v] = True
            if v == e:
                break
            for child in self.graph[v]:
                if child not in discovered:
                    queue.append(child)
                    parent[child] = v
                    discovered[child] = True

        shortest_path = []
        shortest_path.append(e)
        curr_node = parent[e]
        while curr_node:
            shortest_path.append(curr_node)
            curr_node = parent[curr_node]
        print(shortest_path)


# first we create the adjacency matrix
def create_adj_mat(n, roads):
    """create the adjacency matr
    Args:
        n: int,
        m: int, roads
        roads: list(tuple(int, int)), list of roads
    returns:
        list(tuple(int, int)): the mat with the edge information
    """
    cities = [0]*n
    cities = [[0]*n for _ in range(n)]
    for x, y in roads.items():
        cities[x][y] = 1;cities[y][x] = 1
    return cities

def get_side_roads(main_roads):
    """
    create the side roads from the main road
    args:
        main_roads: List[List[int]], 2d mat of the roads connection
    returns:
        list(tuple(int, int)): 2d array with the side roads information
    """
    return [[n^1 for n in m] for m in main_roads]

def create_adjacency_list(n, side_roads):
    """
    create the graph from side roads.
    argos:
        side_roads (list(tuple(int, int))): side roads matrix
    returns:
        Graph: the graph for further processing
    """
    g = Graph()
    for u, v in itertools.product(range(n), range(n)):
        if side_roads[u][v] == 1:
            if u == v:
                g.add_edge(u, v)
    return g

def get_lookup(lookup, val):
    if val in lookup:
        a = lookup.index(val)
    else:
        lookup.append(val)
        a = len(lookup) - 1
    return a, lookup

def get_start(lookup, v):
    for i, c in lookup:
        if c == v:
            return i

def rust_murderer(n, roads, s):
    lookup = []
    roads_mapping = {}
    for i, j in roads:
        a, lookup = get_lookup(lookup, i)
        b, lookup = get_lookup(lookup, j)
        roads_mapping[a] = b
    print(lookup)
    print(roads_mapping)
    cities = create_adj_mat(n, roads_mapping)
    print("cities:", cities)
    side_roads = get_side_roads(cities)
    print("side_roads", side_roads)
    g = create_adjacency_list(n, side_roads)
    print("full graph", g.graph)
    lookup = [(i,v) for i, v in enumerate(lookup)]
    lookup = sorted(lookup, key=lambda x: x[1])
    # lookup = {value in matrix : actual city value}
    start = get_start(lookup, s)
    for other_cities in lookup:
        oc = other_cities[0]
        if oc != start:
            g.bfs(start, oc)

rust_murderer(4, [[1, 2], [2, 3], [1, 4]], 1)
