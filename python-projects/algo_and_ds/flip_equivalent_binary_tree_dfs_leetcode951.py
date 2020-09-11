# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root1, root2):
        flipped = False
        if root1 and root2:
            leftnode1 = root1.left
            rightnode1 = root1.right
            leftnode2 = root2.left
            rightnode2 = root2.right
            if leftnode1 and leftnode2 and rightnode1 and rightnode2:
                if leftnode1.val == leftnode2.val and rightnode1.val == rightnode2.val:
                    check1 = self.dfs(root1.left, root2.left)
                    check2 = self.dfs(root1.right, root2.left)
                elif leftnode1.val == rightnode2.val and rightnode1.val == leftnode2.val:
                    check1 = self.dfs(root1.left, root2.right)
                    check2 = self.dfs(root1.left, root2.right)
                else:
                    return False
                return check1 and check2
            elif leftnode1 and leftnode2:
                if leftnode1.val == leftnode2.val:
                    return self.dfs(leftnode1, leftnode2)
                else:
                    return False
            elif leftnode1 and rightnode2:
                if leftnode1.val == rightnode2.val:
                    return self.dfs(leftnode1, rightnode2)
                else:
                    False
            elif rightnode1 and leftnode2:
                if rightnode1.val == leftnode2.val:
                    return self.dfs(rightnode1, leftnode2)
                else:
                    return False
            else: # all the children are null
                return True
        elif root1 or root2:
            return False
        else:
            return True
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1, root2)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None or root2 is None:
            return root1 is None and root2 is None
        return root1.val == root2.val and (
            (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        )

the above solution is the correct one.
