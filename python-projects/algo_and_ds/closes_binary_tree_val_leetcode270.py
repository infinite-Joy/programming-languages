#270. Closest Binary Search Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# this can be done using the validate binary search  tree approach
# we will find the bigger and the smaller elements
# and then finally see from which the difference is less
# time complexity O(logn)
# space complexity O(1)
from math import inf, fabs
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        between = [None, None]
        while root:
            if target < root.val:
                between[1] = root
                root = root.left
            elif target > root.val:
                between[0] = root
                root = root.right
            else:
                return root.val
        if between == [None, None]:
            return None
        elif between[0] is None:
            return between[1].val
        elif between[1] is None:
            return between[0].val
        else:
            leftdiff = fabs(between[0].val - target)
            rightdiff = fabs(between[1].val - target)
            if leftdiff > rightdiff:
                return between[1].val
            else:
                return between[0].val
