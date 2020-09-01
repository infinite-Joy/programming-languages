"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

serialise and deserialize a binary tree

maybe we can use bfs  for this
and then we will

                1
        2               3
    4       N         N   5

    1;2;3;4;N;N;5;N;N;N;N

    1 -> put 1 in the queue, level 1, next level = 2**1 -> [1]
    2 -> take 1 from the queue 2 is the left, put 2 in the queue
        take 3 put 3 to the right, put 3 in the queue -> [2, 3]


    4; N -> take 2 from queue 2.left = 4, 2.right = None. put 4 and none into the queue -> [3, 4, NOne]

    N: 5 -> take 3 from queue. 3.left = none, 3.right = 5, put 3 and none into the queue -> [4, none, none, 5] no need to put none into the queue

    n,n -> take 4 from queue, 4.left = none, 4.right = none

    n,n -> take 5 from queue, 5.left = none, 5.right = none

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    def _serialize(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                yield str(node.val)
            else:
                yield 'n'
            if node:
                for child in [node.left, node.right]:
                    queue.append(child)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None: return ""

        return ';'.join([s for s in self._serialize(root)])


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None

        data = data.split(';')
        root = TreeNode(int(data[0]))
        queue = deque([root])

        data_iter = iter(data[1:]) # root is already taken care of

        for left in data_iter:
            right = next(data_iter)
            leftnode = TreeNode(int(left)) if left != 'n' else None
            rightnode = TreeNode(int(right)) if right != 'n' else None
            parent = queue.popleft()
            parent.left = leftnode
            parent.right = rightnode
            if leftnode:
                queue.append(leftnode)
            if rightnode:
                queue.append(rightnode)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
