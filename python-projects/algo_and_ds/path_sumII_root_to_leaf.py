# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        # edge case
        if root is None:
            return []
        
        def dfs(root, pathsum):
            if root.left is None and root.right is None: # leaf
                pathsum = pathsum + root.val
                if pathsum == targetSum:
                    return True, [[root.val]]
                else:
                    return False, []
            else:
                leftcomb = []
                lpossible = None
                if root.left:
                    # print('left root', root.left)
                    lpossible, leftcomb = dfs(root.left, pathsum+root.val)
                    # print('23', lpossible, leftcomb)
                    if lpossible:
                        leftcomb = [x + [root.val] for x in leftcomb]
                    else:
                        leftcomb = leftcomb
                rightcomb = []
                rpossible = None
                if root.right:
                    rpossible, rightcomb = dfs(root.right, pathsum+root.val)
                    # print('32 rightcomb', rightcomb, root.val, pathsum)
                    if rpossible:
                        # print('34', rightcomb[0].append(, root.val)
                        rightcomb = [x + [root.val] for x in rightcomb]
                        # print('35', rightcomb)
                    else:
                        rightcomb = rightcomb
                # print('leftcomb, rightcomb', leftcomb, rightcomb)
                return lpossible or rpossible, leftcomb + rightcomb
            
        _, comb = dfs(root, 0)
        comb = [x[::-1] for x in comb]
        return comb