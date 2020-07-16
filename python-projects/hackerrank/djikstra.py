"""
Find single source shortest path using djikstra

reference https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/DijkstraShortestPath.java

space complexity - O(E+V)
time complexity - O(ElogV)
"""

import heapq
from functools import total_ordering
from collections import defaultdict
import math


@total_ordering
class Item:
    def __init__(self, priority, index, val):
        self.priority = priority
        self.index = index
        self.val = val

    def __repr__(self):
        return "Item(priority={}, index={}, val={})".format(
            self.priority, self.index, self.val)

    def __str__(self):
        return repr(self)

    def __lt__(self, other):
        return (self.priority, self.index) < (other.priority, other.index)

    def __eq__(self, other):
        return (self.priority, self.index) == (other.priority, other.index)

a = Item(3, 1, 'a')
b = Item(1, 2, 'b')
c = Item(1,2,'c')

print(a < b)
print(b<c)
print(b == c)

pq = [ ]
heapq.heappush(pq, Item(3, 1, 'a'))
heapq.heappush(pq, Item(5, 2, 'b'))
heapq.heappush(pq, Item(3,2,'c'))
priority = heapq.heappop(pq)
print(priority)
priority.priority = 4
print(priority)


class BinaryMinHeap:
    """
    Combination of binary heap and hash map

    Supporting  the following operations

    * extract_min: O(logn)
    * add: O(logn)
    * change_key_priority: O(logn)
    * contains_key: O(1)
    * get_key_weight: O(1)

    """
    def __init__(self):
        self._queue = []
        self.index = 0
        self.keys = {}

    def __repr__(self):
        return "queue: {}, keys: {}".format(repr(self._queue), repr(self.keys))

    def __bool__(self):
        """For checking the truthiness of this class.

        Returns false if the queue and keys are empty
        """
        return len(self._queue) > 0 or len(self.keys) > 0

    def add(self, val, priority):
        item = Item(priority, self.index, val)
        heapq.heappush(self._queue, item)
        self.keys[val] = item
        self.index += 1

    def contains(self, key):
        return key in self.keys

    def extract_min(self):
        item = heapq.heappop(self._queue)
        del self.keys[item.val]
        return item

    def get_key_weight(self, k):
        return self.keys[k].priority

    def get_item(self, k):
        return self.keys[k]

    def change_key_priority(self, k, v):
        self.keys[k].priority = v
        heapq.heapify(self._queue)


print('binary min heap implementation')
heap = BinaryMinHeap()
heap.add('a', 5)
heap.add('b', 2)
heap.add('c', 3)
print(heap._queue)
print(heap._queue)
print(heap.contains('a'))

heap.change_key_priority('b', 10)
print(heap._queue)
print(heap.extract_min())
print(heap._queue)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edges(self, u, vs, ws=None, undirected=True):
        """
        Add edges takes in the output edges in an undirected graph.

        Args:
            u (str/int): the starting node ids
            vs list(str/int): the edge node ids
            ws list(int): the weights of the ids

        Returns:
            None: but updates the graph
        """
        # if weights not given initialise all of them as 1
        if ws is None:
            ws = [1 for _ in vs]

        self.graph[u].extend(list(zip(vs, ws)))
        self.vertices.add(u)
        self.vertices.update(vs)

        # for the opposite case if undirected
        if undirected is True:
            for v, w in zip(vs, ws):
                self.graph[v].append((u, w))

    def add_edge(self, u, v, w=None, undirected=True):
        """
        SImilar to add edges

        Args:
            u (str/int): the first node
            v (str/int): the second node id
            w (int): the edge weight

        Returns:
            None: but updates the graph
        """
        if w is None:
            w = 1

        self.graph[u].append((v,w))
        self.vertices.add(u)
        self.vertices.add(w)

        # for the opposite case if undirected
        if undirected is True:
            self.graph[v].append((u,w))

    def get_all_vertices(self):
        return iter(self.vertices)

    def get_edges(self, u):
        return self.graph[u]


class DjikstraShortestPath:
    """
    djikstra is a modified version of the bfs when the edge weights are given
    and hence we need a priority queue based on the edge weights
    """
    @staticmethod
    def shortest_path(graph, source):
        # heap + map data structure
        min_heap = BinaryMinHeap()

        # stores shortest distance from root to each of the vertex
        distance = []

        # stores parent of each vertex in the shortest distance
        parent = {}

        # initialise all vertex with infinite distance from the source vertex
        for vertex in graph.get_all_vertices():
            min_heap.add(vertex, math.inf)

        # set distance of source vertex to 0
        min_heap.change_key_priority(source, 0)

        # put it on the map
        source_node = min_heap.get_item(source)
        distance.append(source_node)

        # before the source there was the big bang
        parent[source] = None

        while min_heap:
            #__import__('pdb').set_trace()

            # get the min value from heap node which has vertex and distance of
            # that vertex from source vertex.
            heap_node = min_heap.extract_min()
            current = heap_node.val

            # update shortest distance of current node from source vertex
            distance.append(heap_node)

            # iterate through all edges of current vertex
            for adjacent_vertex, weight in graph.get_edges(current):

                # do this only if there is vertex in the min heap and that has
                # not been processed yet
                if min_heap.contains(adjacent_vertex):

                    adjacent_vertex_item = min_heap.get_item(adjacent_vertex)

                    # add distance of current vertex to get distance of
                    # adjacent vertex from source  vertex when it goes through
                    # current vertex
                    new_distance = heap_node.priority + weight

                    # see if the calculated distance is less than the current
                    # distance and then update the distance
                    if new_distance < adjacent_vertex_item.priority:
                        min_heap.change_key_priority(
                            adjacent_vertex, new_distance)
                        parent[adjacent_vertex] = current

        return distance, parent

print("#"*20)
print("implementing djikstra")
# driver
graph = Graph()
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 8)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 4, 9)
graph.add_edge(4, 5, 10)
graph.add_edge(2, 5, 4)
graph.add_edge(1, 7, 11)
graph.add_edge(0, 7, 8)
graph.add_edge(2, 8, 2)
graph.add_edge(3, 5, 14)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 8, 6)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 8, 7)

graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 2)
graph.add_edge(1, 4, 9)
graph.add_edge(1, 5, 3)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 4, 2)
graph.add_edge(3, 4, 3)

djikstra_shortest_path = DjikstraShortestPath()
source = 1
distance, parent = djikstra_shortest_path.shortest_path(graph, source)
print(distance, parent)
