"""

285. Inorder Successor in BST

this should be done using morris traversal

because in any case is is going to be O(n)

but we should not be using stack for this

                    [6,2,8,0,4,7,9,null,null,3,5]
                    6
            2               8
        0       4       7       9
              3    5

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def find_predecessor(self, node):
        pred = node.left
        while pred.right and pred.right != node:
            pred = pred.right
        return pred
    def find_succ(self, node):
        nnode = node.right
        while nnode.left:
            nnode = nnode.left
        return nnode
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root and p:
            isleaf = p.right is None
            # if not leaf we can use the simple inorder traversal
            if isleaf:
                # using the morris traversal
                node = root
                while node:
                    if node.left is None:
                        if node.val == p:
                            return node.right
                        node = node.right
                    else:
                        pred = self.find_predecessor(node)
                        if pred.right is None:
                            pred.right = node
                            node = node.left
                        else:
                            pred.right = None
                            if node.val == p:
                                return node.right
                            node = node.right
            else:
                return self.find_succ(p)



# test code

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

null = None
data = [6,2,8,0,4,7,9,null,null,3,5]
sol = Solution()
root = serialise(data)
print(sol.inorderSuccessor(root, 2))
