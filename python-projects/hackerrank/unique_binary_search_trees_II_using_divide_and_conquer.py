"""
A divide and conquer algo for unique binary trees.

The run time of this is O(n2) as this checks through the trees again and again

but can be easily converted to a DP solution

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder_traversal(self, root):
        if root is None:
            yield None
        else:
            yield root.val
            if root.left is None:
                yield None
            else:
                yield from self.preorder_traversal(root.left)
            if root.right is None:
                yield None
            else:
                yield from self.preorder_traversal(root.right)

    def __repr__(self):
        root = self
        return " ".join(map(lambda x: str(x),
                            self.preorder_traversal(root)))


# memoised solution
def generate(start, end, memo):
    print(start, end, memo)
    if (start, end) in memo:
        return memo[(start, end)]
    elif start > end:
        return [None]
    else:
        res = []
        for i in range(start, end+1):
            memo[(start, i-1)] = generate(start, i-1, memo)
            lefttrees = memo[(start, i-1)]
            memo[(i+1, end)] = generate(i+1, end, memo)
            righttrees = memo[(start, i-1)]

            for lefttree in lefttrees:
                for righttree in righttrees:
                    root = TreeNode(i)
                    root.left = lefttree
                    root.right = righttree
                    res.append(root)
        memo[(start,end)] = res
        return memo[(start,end)]


def generate_trees(n):
    if n == 0:
        print([])
    for tree in generate(1, n, {}):
        pass

generate_trees(4)

# dp solution
def generate_trees_dp(n):
    i = end
    dp = [[] for x in range(1, n+1)]
    dp[0] = None
    for start in range(n, -1, -1): # this is the root
        for s in range(n, start-1, -1):
            node = TreeNode(s)
            node.right =

