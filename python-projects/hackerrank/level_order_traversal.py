"""
Finding the level order
a simple way would be to save the height as part of the queue as well and then save the next part of the queue with the height as well
once we have the solution in place then build the nested array.
keep a variable to get the height as well or the maximum height
===================================

space complexity : O(V)
time complexity: O(V)

you dont need the E part of the general graph as you dont need to maintain the
E component for the bfs and the dfs
"""
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return "Node - {}".format(self.val)

def process_vertex_early(level_order, node, h):
    if len(level_order) == h:
        level_order[h-1].append(node.val)
    else:
        level_order.append([node.val])
    return level_order

def bfs(root):
    level_order = []
    queue = deque([(root, 1)])
    while queue:
        node, h = queue.popleft()
        level_order = process_vertex_early(level_order, node, h)
        print(node, h, level_order)
        if node.children is not None:
            for child in node.children:
                queue.append((child, h+1))
    return level_order

# driver
root = Node(1)
two, three, four, five = Node(2), Node(3), Node(4), Node(5)
root.children = [two, three, four, five]
six, seven = Node(6), Node(7)
three.children = [six, seven]
eight = Node(8)
four.children = [eight]
nine, ten = Node(9), Node(10)
five.children = [nine, ten]
eleven = Node(11)
seven.children = [eleven]
twelve = Node(12)
eight.children = [twelve]
thirteen = Node(13)
nine.children = [thirteen]
fourteen = Node(14)
eleven.children = [fourteen]

print(bfs(root))

