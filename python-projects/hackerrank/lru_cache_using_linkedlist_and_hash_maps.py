146. LRU Cache
https://leetcode.com/problems/lru-cache/
get or set  the value if the key is not already present
using a get and a put
this can be done using a linked list queue and dict
get(k):
    if value not in dict: return -1
    if value in dict:
        take the value and put it at the end of the queue
        end = node
put(k, v):
    if k in dict: pass
    else:
        put node at the end of the queue
        end = node
        size += 1
        if size == capacity:
            start = start.next
            size -= 1
printitems:
    next_node = start
    while next_node is not none:
        yield next_node
        next_node = next_node.next
==================================================================
class Node:
    def __init__(self, key, value, next=None):
        self.value = value
        self.key = key
        self.next = next
    def __repr__(self):
        return “Node: key: {}, value: {}”.format(self.key, self.value)
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0 # the current size of the queue, maximum value is capacity
        self.start = None
        self.end = None
        self.mapping = {} # will have the keys and the values are the nodes in the queue
    def get(self, k):
        # complexity O(1)
        if k not in self.mapping:
            return -1
        node = self.mapping[k]
        self.end.next = node
        self.end = node
        return node
    def put(self, k, v):
        # complexity O(1)
        if k not in self.mapping:
            node = Node(k, v)
            self.mapping[k] = node
            self.end = node
            if self.size == 0:
                self.end = self.start
            size += 1
            if self.size == self.capacity:
                start = self.start
                del self.mapping[start.key]
                self.start = self.start.next
                self.size -= 1
    def print_items(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

