"""
Please implement a program that lists the nodes of a random binary tree by nodes at the same depth.
"""

class Node:
    '''class that builds up the node'''

    def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __str__(self):
            return '%s' % self.data


class ListAtSameDepth:
    '''methods to parse the node'''

    def height(self, root):
            if root is None:
                return 0
            return 1 + max(self.height(root.left), self.height(root.right))

    def printKDistant(self, root, k):
            if root is None:
                return

            if k == 0:
                print(root.data, end= " ")
            else:
                self.printKDistant(root.left, k-1)
                self.printKDistant(root.right, k-1)


# below is the driver code
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.right = Node(14)
root.right.right.left = Node(15)

lasd = ListAtSameDepth()

ht = lasd.height(root)

for i in range(ht):
    lasd.printKDistant(root, i)
    # we print a new line to separate with a new line the nodes at same depth
    print()
"""
#################################################
Output:

➜ python list_nodes_at_same_depth.py
1
2 3
4 5 7 6
8 9 10 11 12 13 15 14

"""
