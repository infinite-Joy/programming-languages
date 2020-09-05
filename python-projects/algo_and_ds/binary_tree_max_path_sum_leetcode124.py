"""

binary tree max path sum

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

so basic idea is recursion
    go to the left sub tree
    see the sum
    go to the right sub tree
    and then update the max in this way

the time complexity: O(nodes in the full tree)
space complexity: O(height of the tree) which is log(nodes) if the tree is balanced and leaves if unbalanced

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def __init__(self):
        self.maxsum = -inf
    def postorder(self, root):
        if root:
            leftsum = max(0, self.postorder(root.left))
            rightsum = max(0, self.postorder(root.right))
            self.maxsum = max(leftsum + rightsum + root.val, self.maxsum)
            return max(leftsum + root.val, rightsum + root.val)
        else:
            return 0
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None: return 0
        val = self.postorder(root)
        # print(self.maxsum)
        # print(val)
        return max(self.maxsum, val)

