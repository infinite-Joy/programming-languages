"""

https://www.careercup.com/question?id=5749533368647680

similar problem https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given the root of a binary tree containing integers, print the columns of the tree in order with the nodes in each column printed top-to-bottom.

Input:
      6
     / \
    3   4
   / \   \
  5   1   0
 / \     /
9   2   8
     \
      7

Output:
9 5 3 2 6 1 7 4 8 0

Input:
       1
     /   \
    2     3
   / \   / \
  4   5 6   7

When two nodes share the same position (e.g. 5 and 6), they may be printed in either order:

Output:
4 2 1 5 6 3 7
or:
4 2 1 6 5 3 7

understood this from leetcode

do a preorder traversal and save it in the hashmap which the level of the columns
then sort the hashmap and print it Out

to not do the sorting again we will be implementing the inorder which will keep the keys sorted from left to right

time complexity is O(n).
space complexity is O(n)

"""

from typing import List
from collection import OrderedDict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode, levels: Dict[int, List[List[int]]], level: int):
    if root is not None:
        inorder(root.left, levels, level-1)
        if level not in levels:
            levels[level] = []
        levels[level].append(root.val)
        inorder(root.right, levels, level+1)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return [[None]]
        levels = OrderedDict()
        inorder(root, levels, 0)

        levels = list(levels.items())
        return [v for _, v in levels]
