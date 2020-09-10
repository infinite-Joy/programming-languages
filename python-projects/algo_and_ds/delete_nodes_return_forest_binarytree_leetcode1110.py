"""

delete nodes and return forest

leetcode 1110

convert to_delete to a set
do dfs on the tree.
if we find the node make the changes, put the root in to the solution and then start the dfs on the remaining edges

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sol = {}
    def process_matched_node(self, pred, node, to_delete):
        if pred:
            if pred.right == node:
                pred.right = None
            else:
                pred.left = None
        if node.left:
            self.sol[node.left.val] = node.left
        if node.right:
            self.sol[node.right.val] = node.right
        self.postorder(None, node.left, to_delete)
        self.postorder(None, node.right, to_delete)
    def postorder(self, pred, node, to_delete):
        if node and to_delete:
            if node.val in to_delete:
                if node.val in self.sol:
                    del self.sol[node.val]
                to_delete.remove(node.val)
                self.process_matched_node(pred, node, to_delete)
            else:
                self.postorder(node, node.left, to_delete)
                self.postorder(node, node.right, to_delete)
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.sol[root.val] = root
        self.postorder(None, root, to_delete)
        return list(self.sol.values())
