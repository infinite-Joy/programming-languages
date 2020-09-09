"""

house robber III

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

implement bfs and add all the even to even and odd to odd

"""

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, root, even_odd_sum):
        queue = deque([root, 0])
        while queue:
            node, level = queue.popleft()
            even_odd_sum[level] += node.val
            for child in [node.left, node.right]:
                queue.append((child, level ^ 1)) # to flip we can also make it 1 - level
    def rob(self, root: TreeNode) -> int:
        even_odd_sum = [0, 0]
        self.bfs(root, even_odd_sum)
        return max(even_odd_sum)


# this is not working out. need a different approach

class Solution:
    def postorder(self, root):
        if not root: return 0

        robleft = self.postorder(root.left)
        robright = self.postorder(root.right)

        robnow = robleft[1] + robright[1] + root.val
        roblater = max(robleft) + max(robright)

        return roblater, robnow

    def rob(self, root: TreeNode) -> int:
        return max(self.postorder(root))
