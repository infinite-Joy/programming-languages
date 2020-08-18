#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the balancedForest function below.
# we can create all combinations of the edges
# and then we can check the sum of the trees.
# this can also be done in a greedy manner. somewhat
# check the amount to the leaves. check if the other
# vales also match to the same amount
from itertools import product
from typing import Set, List

class Node:
    def __init__(self, id: int, val: int):
        self.id = id
        self.val = val
        self.children = []
    def add_edge(self, other: 'Node'):
        self.children.append(other)
    def get_children(self, exclude: Set[int]):
        for child in self.children:
            if child.id not in exclude:
                yield child

def dfs(root, exclude, sumval):
    sumval += root.val
    for child in root.get_children(exclude):
        sumval = dfs(child, exclude, sumval)
    return sumval

def compare(root1, root2, root3, exclude):
    sum1 = dfs(root1, exclude, 0)
    sum2 = dfs(root2, exclude, 0)
    sum3 = dfs(root3, exclude, 0)
    print(sum1, sum2, sum3)
    if sum1 == sum2 and sum1 > sum3:
        return sum1 - sum3
    if sum1 == sum3 and sum1 > sum2:
        return sum1 - sum2
    if sum2 == sum3 and sum2 > sum1:
        return sum2 - sum1

from math import inf

def balancedForest(c, edges):
    data_values = c
    # have a list of nodes
    nodes = [None]
    for i, val in enumerate(data_values, 1):
        nodes.append(Node(i, val))
    # create the edge pointers
    for node1, node2 in edges:
        nodes[node1].add_edge(nodes[node2])

    minval = inf
    for edge1, edge2 in product(edges, edges):
        if edge1 != edge2:
            node1, node2 = edge1
            node3, node4 = edge2
            root1 = nodes[1]
            root2 = nodes[node2]
            root3 = nodes[node4]
            exclude = {node2, node4}
            val = compare(root1, root2, root3, exclude)
            print(edge1, edge2, val)
            val = val if val else inf
            minval = min(minval, val)

    return minval if minval is not inf else -1

data_values = [1,1,2,2,1]
edges = [
    [1,2], [1,3], [3,5], [1,4]
]
print(balancedForest(data_values, edges))

data_values = [1,3,5]
edges = [
    [1,3], [1,2]
]
print(balancedForest(data_values, edges))
