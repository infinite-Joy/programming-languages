"""
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
"""


class Node:
    def __init__(self, key, value, parent=None, next=None):
        self.value = value
        self.key = key
        self.next = next
        self.parent = parent

    def __repr__(self):
        return "Node: key: {}, value: {}".format(self.key, self.value)


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

        # if node is the end then nothing to do
        if node == self.end: pass
        elif node == self.start: # node is the start
            self.start = self.start.next
            self.start.parent = None
            self.end.next = node
            node.parent = self.end
            self.end = node
            self.end.next = None
        else: # somewhere in the middle
            # detach node is not the end
            prev_node = node.parent
            next_node = node.next
            prev_node.next = next_node
            next_node.parent = prev_node

            # attach node at the end
            self.end.next = node
            node.parent = self.end
            self.end = node
            self.end.next = None

        print(self)
        return node

    def put(self, k, v):
        # complexity O(1)
        #__import__('pdb').set_trace()
        if k not in self.mapping:
            node = Node(k, v)
            self.mapping[k] = node
            if self.size == 0:
                self.end = node
                self.start = self.end
            else:
                self.end.next = node
                node.parent = self.end
                self.end = node
            self.size += 1
            # size reaches the max capcity
            if self.size > self.capacity:
                start = self.start
                del self.mapping[start.key]
                self.start = self.start.next
                self.start.parent = None
                self.size -= 1
        print(self)

    def print_items(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        return "->".join([str((x.key, x.value)) for x in self.print_items()])

cache = LRU(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

# for a linked hash map implementation collections.ordereddict can  be used

from collections import OrderedDict


class LRU_new:
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = OrderedDict()

    def get(self, key):
        # complexity O(1)
        if key not in self.mapping:
            return -1
        value = self.mapping[key]
        self.mapping.move_to_end(key)
        return value

    def put(self, key, value):
        # complexity O(1)
        if key in self.mapping:
            self.mapping.move_to_end(key)
        self.mapping[key] = value
        if len(self.mapping) > self.capacity:
            oldest = next(iter(self.mapping))
            del self.mapping[oldest]

    def __str__(self):
        return "->".join([str((k, v)) for k, v in self.mapping.items()])


print("with the new lru")
cache = LRU_new(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
