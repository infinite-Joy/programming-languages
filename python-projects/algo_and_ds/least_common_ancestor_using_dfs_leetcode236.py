"""

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

to find the lowest common ancestor of two notes in a binary tree

not a binary search tree

that should be noted

using dfs we will be able to find the LCA

using dfs this is O(n)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Doing an inorder traversal
        """
        if root:
            if root == p:
                return p
            if root == q:
                return q

            leftnode = self.lowestCommonAncestor(root.left, p, q)
            rightnode = self.lowestCommonAncestor(root.right, p, q)

            if leftnode and rightnode:
                return root

            return leftnode or rightnode
