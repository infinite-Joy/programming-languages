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


def generate(start, end):
    print(start, end)
    if start > end:
        yield
    else:
        for i in range(start, end+1):
            lefttrees = generate(start, i-1)
            righttrees = generate(i+1, end)

            for lefttree in lefttrees:
                for righttree in righttrees:
                    root = TreeNode(i)
                    root.left = lefttree
                    root.right = righttree
                    yield root


def generate_trees(n):
    if n == 0:
        print([])
    for tree in generate(1, n):
        pass

generate_trees(4)
