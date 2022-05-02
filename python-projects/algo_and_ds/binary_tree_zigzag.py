# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

"""
odd one will have negative sign

"""

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            level_order = []
            queue = deque([(root, 0)]) # node, height
            # visited = {root, visited}
            
            while queue:
                node, h = queue.popleft()
                if node is not None:
                    if h == len(level_order):
                        level_order.append([node.val])
                    else:
                        level_order[h].append(node.val)

                    for child in [node.left, node.right]:
                        queue.append((child, h+1))
            
            for h, elems in enumerate(level_order):
                if h % 2 == 1:
                    level_order[h] = level_order[h][::-1]
                    
            return level_order
        
        return bfs(root)