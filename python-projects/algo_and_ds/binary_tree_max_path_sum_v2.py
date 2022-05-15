# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This is using the post order route.

"""

import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def max_path_sum(root):
            if root is None:
                return -math.inf, -math.inf
            
            left1, left2 = max_path_sum(root.left) # 2,2
            right1, right2 = max_path_sum(root.right) # 3,3
            
            return (
                max(max(left1 + root.val, root.val), max(right1 + root.val, root.val)), # 2, 3 = 3,
                max(left2, right2,
                    max(left1 + root.val, root.val),
                    max(right1 + root.val, root.val),
                    max(left1 + right1 + root.val, root.val)) # 2, 2, 3, 4, 6
            )
        
        straight_path, with_root = max_path_sum(root)
        return max(straight_path, with_root)