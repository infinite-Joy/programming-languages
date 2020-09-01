"""

flatten the binary tree

    1
   / \
  2   5
 / \   \
3   4   6

2.right = 3
2.left = NOne
3.right =4
3.left = NOne
return 2, 4


"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return "Node({})".format(self.val)

def serialise(data):
    root = TreeNode(int(data[0]))
    queue = deque([root])
    data_iter = iter(data[1:]) # root is already taken care of
    for left in data_iter:
        right = next(data_iter)
        leftnode = TreeNode(int(left)) if left else None
        rightnode = TreeNode(int(right)) if right else None
        parent = queue.popleft()
        parent.left = leftnode
        parent.right = rightnode
        if leftnode:
            queue.append(leftnode)
        if rightnode:
            queue.append(rightnode)

    return root

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #__import__('pdb').set_trace()
        if root:
            left = root.left
            right = root.right
            print(root.val)
            start, end = self.flatten(left)
            if not end: end = start

            if start:
                root.right = start
                root.left = None
                end.right = right
                end.left = None

            start, end = self.flatten(right)
            return root, right
        return None, None

# test  case

data = [1,2,5,3,4,None,6]
s = Solution()
root = serialise(data)

s = Solution()
s.flatten(root)
#__import__('pdb').set_trace()

# (Pdb) root.right.right
# Node(3)
# (Pdb) root.right.right.right
# Node(4)
# (Pdb) root.right.right.right.right
# Node(5)
# (Pdb) root.right.right.right.right.right
# Node(6)
# (Pdb) root.right.right.right.right.right.right
# (Pdb)

data = [1,2,None,3,4]
s = Solution()
root = serialise(data)
s.flatten(root)
__import__('pdb').set_trace()
