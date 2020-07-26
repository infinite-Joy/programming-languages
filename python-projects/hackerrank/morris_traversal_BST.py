"""
Morris traversal using iteration

time complexity: O(n)
space complexity: O(1)

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node({})".format(self.val)


def find_predecessor(root):
    before = root.left
    while before.right is not None and before.right.val < root.val:
        before = before.right
    return before


def morris_traversal(root):
    while root is not None:
        if root.left is None:
            yield root
            root = root.right
        else:
            predecessor = find_predecessor(root)
            if predecessor.right is None:
                predecessor.right = root
                root = root.left
            else:
                predecessor.right = None
                yield root
                root = root.right

# driver
root = Node(
    10,
    Node(5, Node(2), Node(7)),
    Node(15, None, Node(30))
)

for node in morris_traversal(root):
    print(node)
