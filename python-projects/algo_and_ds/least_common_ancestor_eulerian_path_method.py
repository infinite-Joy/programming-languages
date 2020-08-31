"""
referemce for this is here

https://www.youtube.com/watch?v=sD1IoalFomA
https://www.youtube.com/watch?v=uUatD9AudXo

"""

from math import floor, log2
import numpy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def __init__(self):
        self.nodes = None
        self.depth = None
        self.last = None
        self.tour_index = 0
        self.sparse_table = None
        self.node_count = 0
        self.node_identifiers = {}

    def visit(self, node, depth):
        self.nodes[self.tour_index] = node
        self.depth[self.tour_index] = depth
        self.last[self.node_identifiers[node.val]] = self.tour_index
        self.tour_index += 1
        print(self.nodes)
        print(self.depth)
        print(self.last)
        import time; time.sleep(1)

    def dfs(self, root, depth):
        if root:
            self.visit(root, depth)
            for child in [root.left, root.right]:
                if child is not None:
                    self.dfs(child, depth+1)
                    self.visit(root, depth)

    def create_min_sparse_table(self, depth):
        P = floor(log2(len(depth)))
        dp = [[None for _ in depth] for _ in range(P+1)]
        dp[0] = depth[:]
        #print(numpy.matrix(dp))
        for i in range(1, P+1):
            for j in range(len(depth)):
                compare_with = j + 2**(i-1)
                if compare_with < len(depth) and dp[i-1][compare_with] is not None:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][compare_with])
            #import time; time.sleep(1)
            #print(dp[i])
        return dp

    def query_index(self, left, right):
        # first find the value of p, which gives the largest 2**p that fits in
        # the range between left and right
        len = right - left + 1
        p = floor(log2(len))
        k = 2**p
        return min(
            self.sparse_table[p][left], self.sparse_table[p][right - k + 1])

    def setup(self, root, n):
        # array of nodes of size 2n - 1
        self.nodes = [None for _ in range(2*n - 1)]

        # array of integers of size 2n - 1
        self.depth = [None for _ in range(2*n - 1)]

        # node index -> Euler tour index
        self.last = [None for _ in range(n)]

        # do eulerian tour around the tree
        self.dfs(root, 0)
        #print(self.nodes)
        #print(self.depth)
        #print(self.last)

        # initialise the sparse table data structure to do Range Minimum
        # queries on the depth array. Sparse tables take O(nlogn) time to
        # construct and O(1) time to do queries
        # provided they are associative and overlap friendly
        self.sparse_table = self.create_min_sparse_table(self.depth)
        #print(numpy.matrix(self.sparse_table))

    def get_lca(self, p, q):
        eulerian_p = self.last[self.node_identifiers[p.val]]
        eulerian_q = self.last[self.node_identifiers[q.val]]

        left = min(eulerian_p, eulerian_q)
        right = max(eulerian_p, eulerian_q)
        min_val_idx = self.query_index(left, right)

        return self.nodes[min_val_idx]

    def count(self, root):
        if root:
            self.node_identifiers[root.val] = self.node_count
            self.node_count += 1

            self.count(root.left)
            self.count(root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            self.count(root)
            self.setup(root, self.node_count)
            lca = self.get_lca(p, q)
            return lca

# test case
root = TreeNode(3)
n5 = TreeNode(5)
n6 = TreeNode(6)
n2 = TreeNode(2)
n7 = TreeNode(7)
n4 = TreeNode(4)
n1 = TreeNode(1)
n0 = TreeNode(0)
n8 = TreeNode(8)
root.left = n5
root.right = n1
n5.left = n6
n5.right = n2
n1.left = n0
n1.right = n8
n2.left = n7
n2.right = n4

#s = Solution()
#print(s.lowestCommonAncestor(root, n5, n4))
#s = Solution()
#print(s.lowestCommonAncestor(root, n6, n4))
#s = Solution()
#print(s.lowestCommonAncestor(root, n7, n8))

# test case 2
n1 = TreeNode(1)
n2 = TreeNode(2)
n1.right = n2
s = Solution()
print(s.lowestCommonAncestor(n1, n1, n2))
