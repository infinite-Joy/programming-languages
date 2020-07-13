import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, lower_bound=-math.inf, upper_bound=math.inf) -> bool:
        print(root.val, lower_bound, upper_bound)
        if root is None:
            return True

        if not lower_bound < root.val < upper_bound:
            return False

        if root.left is not None:
            if not self.isValidBST(root.left, lower_bound, root.val):
                return False

        if root.right is not None:
            if not self.isValidBST(root.right, root.val, upper_bound):
                return False

        return True


# driver
x = TreeNode(10)
x.left = TreeNode(5)
x.right = TreeNode(15)
x.right.left = TreeNode(14)
x.right.right = TreeNode(20)
x.right.left.left = TreeNode(13)
x.right.left.left.left = TreeNode(6)

print(Solution().isValidBST(x))
