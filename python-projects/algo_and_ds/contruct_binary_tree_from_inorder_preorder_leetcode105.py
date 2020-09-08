"""
this was asked to me in the facebook interview

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

preorder = root left right
inorder = left root right


algo is recursive

    func preorder preorderstart preorderend inorder inorderstart inorderend:
        rootval = first value of preorder is the root = preorder[preorderstart]
        rootnode = TreeNode(rootval)

        inorderrootpos = rootval position in inorder arr
        leftinorderstart = inorderstart
        leftinorderend = in inorder all elements on the left belong to the left subtree = inorderrootpos - 1
        rightinorderstart = in inorder all elements on the right belong to the right subtree = inorderrootpos + 1
        rightinorderend = inorderend
        leftpreorderstart = in inorder after the root, the next element is the root of the left subtree = preorderstart + 1
        leftpreorderend = preorder root pos + number of elements in left = preorderstart + leftinorderend - leftinorderstart + 1
        rightpreorderstart = in inorder right subtree starts from where the left subtree ends = leftpreorderend + 1
        rightpreorderend = preorderend

        rootnode.left = func preorder preorderstart preorderend inorder leftinorderstart leftinorderend
        rootnode.right = func preorder preorderstart preorderend inorder rightinorderstart rightinorderend
        return rootnode

"""

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'Node: ' + str(self.val)

class Solution:
    def helper(self, preorder, preorderstart, preorderend, inorder, inorderstart, inorderend):
        if preorderstart > preorderend:
            return None

        print(preorder, preorderstart, preorderend, inorder, inorderstart, inorderend)

        rootval = preorder[preorderstart]
        inorderrootpos = inorder.index(rootval)
        leftinorderstart = inorderstart
        leftinorderend = inorderrootpos - 1
        rightinorderstart = inorderrootpos + 1
        rightinorderend = inorderend
        leftpreorderstart = preorderstart + 1
        leftpreorderend = preorderstart + leftinorderend - leftinorderstart + 1
        rightpreorderstart = leftpreorderend + 1
        rightpreorderend = preorderend

        # build the left and right subtrees
        leftnode = self.helper(preorder, leftpreorderstart, leftpreorderend, inorder, leftinorderstart, leftinorderend)
        rightnode = self.helper(preorder, rightpreorderstart, rightpreorderend, inorder, rightinorderstart, rightinorderend)

        rootnode = TreeNode(rootval)
        rootnode.left, rootnode.right = leftnode, rightnode
        print(preorder, preorderstart, preorderend, inorder, inorderstart, inorderend)

        return rootnode

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
root = sol.buildTree(preorder, inorder)

# Function to print binary tree in 2D
# It does reverse inorder traversal
COUNT = [10]

def print2DUtil(root, space) :

    # Base case
    if (root == None) :
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

print2DUtil(root, 5)
