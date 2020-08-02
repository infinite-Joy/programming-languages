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


class Solution:

    def __init__(self):
        self.first_elem = None
        self.sec_elem = None
        self.prev_elem = TreeNode(-math.inf)

    def recover_tree(self, root: TreeNode):
        # inorder traversal to find the two nodes
        self.inorder(root)

        # swap the values to come up with the original BST tree
        self.first_elem.val, self.sec_elem.val = self.sec_elem.val, self.first_elem.val


    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        # if first element has not been found assign it to the prev elem
        if self.first_elem is None and self.prev_elem.val >= root.val:
            self.first_elem = self.prev_elem

        # if the first element is found then assign the second element to the
        # root
        # this will happen 2 times as there are 2 elements in the tree where
        # this is valid.
        if self.first_elem is not None and self.prev_elem.val >= root.val:
            self.sec_elem = root

        self.prev_elem = root

        self.inorder(root.right)
