"""
two elements are swapped and finding them using BST

time complexity: O(n)
and space complexity is O(logn) since n is the height of the tree

"""

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node({})".self.val


class Solution:

    def __init__(self):
        self.first_elem = None
        self.sec_elem = None
        self.prev_elem = TreeNode(-math.inf)

    def recover_tree(self, root: TreeNode):
        # inorder traversal to find the two nodes
        self.morris_inorder(root)

        # swap the values to come up with the original BST tree
        self.first_elem.val, self.sec_elem.val = self.sec_elem.val, self.first_elem.val

    def find_predecessor(self, root):
        before = root.left
        while before.right is not None and before.right.val != root.val:
            before = before.right
        return before

    def visit(self, root):
        if self.first_elem is None and self.prev_elem.val >= root.val:
            self.first_elem = self.prev_elem
        if self.first_elem is not None and self.prev_elem.val >= root.val:
            self.sec_elem = root
        self.prev_elem = root

    def morris_inorder(self, root):
        while root is not None:
            if root.left is None:
                self.visit(root)
                root = root.right
            else:
                predecessor = self.find_predecessor(root)

                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    self.visit(root)
                    root = root.right

def inorder(root):
    if root is None:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)

s = Solution()
# driver
root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
print([i for i in inorder(root)])
s.morris_inorder(root)
print([i for i in inorder(root)])
