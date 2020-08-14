#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
# since this is the shortest paths we should probably use bfs here.

from collections import deque

def bfs(graph, ids, val):
    queue = deque([(val, 0)])
    visited = set([val])
    while queue:
        node, dist = queue.popleft()
        print(queue, node, dist)
        for neighbor in graph.get(node, []):
            print(neighbor)
            if neighbor not in visited:
                if ids[val - 1] == ids[neighbor - 1]:
                    return dist + 1
                queue.append((neighbor, dist+1))
                visited.add(neighbor)
    return -1

def add_edge(u, v, graph):
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    print(graph_nodes, graph_from, graph_to, ids, val)
    graph = {}
    for u, v in zip(graph_from, graph_to):
        add_edge(u, v, graph)
        add_edge(v, u, graph)
    print(graph)
    return bfs(graph, ids, val)

print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1))
print("#"*10)
print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 3, 4], 1))
print("#"*10)
print(findShortest(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2))
print("#"*10)
