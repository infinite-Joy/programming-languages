# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
the way to do this

left is also BST
right is also BST
max in the left child will be less than root
min in the right child will more than root


"""
import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root):
            if root is None:
                return True, -math.inf, math.inf # validate, max, min

            leftyes, leftmax, leftmin = validate(root.left)
            rightyes, rightmax, rightmin = validate(root.right)
            return (
                leftyes and rightyes and leftmax < root.val and rightmin > root.val,
                max(leftmax, rightmax, root.val),
                min(rightmin, leftmin, root.val)
            )
        return validate(root)[0]
        
        
            