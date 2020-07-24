"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

                4,30
            1,36        6,21
                0,36   2,35           5, 26     7,15
                       3,33                           8,8
so basically something like a reverse in order might work
# Definition for a binary tree node.

time complexity is O(n) since it goes through the whole tree
space complexity is O(h) since at most it would be have the height of the tree in the recursion stack
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def cumulative(self, root: TreeNode, cumsum: int) -> int:
        if root.right:
            cumsum = self.cumulative(root.right, cumsum)
        cumsum = root.val + cumsum
        root.val = cumsum
        if root.left:
            cumsum = self.cumulative(root.left, cumsum)
        return cumsum
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cumulative(root, 0)
        return root

