"""
Find single source shortest path using djikstra

space complexity - O(E+V)
time complexity - O(ElogV)
"""

import heapq
from functools import total_ordering


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
    * contains_key: O(1)
    * get_key_weight: O(1)
    """
