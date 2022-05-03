# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This is the same as doing inorder

"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root
                yield from inorder(root.right)
        
        elem = None
        for i, elem in enumerate(inorder(root)):
            if i+1 == k:
                return elem.val
        return elem.val
            