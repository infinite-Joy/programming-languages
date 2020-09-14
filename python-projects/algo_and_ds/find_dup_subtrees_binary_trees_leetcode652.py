since this is a binary tree approach a recursion would probably make the most sense here
for each root we can have the sum of the trees in the root.
we will return the root of the binary tree
we will make the hashmap with the false and return only the true values at the end
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root, hashmap):
        if root:
            leftsum = self.postorder(root.left)
            rightsum = self.postorder(root.right)
            thisval = leftsum + root.val + rightsum
            if thisval in hashmap;
                hashmap[thisval].append(root)
            else:
                hashmap[thisval] = [root]
            return thisval
        else:
            return 0
    def check_dup(self, node1, node2):
        if node1 is None or node2 is None:
            return node1 is None and node2 is None
        return node1.val == node2.val and self.check_dup(node1.left, node2.left) and self.check_dup(node1.right, node2.right)
def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    hashmap = {}
    sol = []
    self.postorder(root, hashmap)
    for val, nodes in hashmap.items():
        for i in range(len(nodes)):
            for j in range(i + 1, range(len(nodes))):
                if self.check_dup(nodes[i], nodes[j]):
                    sol.append(nodes[i])
    return sol





