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
print("%"*10)

# dp solution

def copy_tree(root):
    root1 = TreeNode(root.val)
    if root.left is not None:
        left1 = copy_tree(root.left)
        root1.left = left1
    if root.right is not None:
        right1 = copy_tree(root.right)
        root1.right = right1
    return root1

def get_val_node(root,val):
    while root is not None:
        if root.val == val:
            return root
        root = root.left

def generate_trees(n):
    if n <= 0:
        return []
    res = [None]
    for num in range(n, -1, -1):
        next_tree = []
        for node in res:
            # the spacial case when Node(n) is root of tree
            root = TreeNode(num)
            root.right = node
            next_tree.append(root)

            # while loop inserts every possible combination to the left tree
            # side
            while node is not None:
                curr_root = TreeNode(root.right.val)

                # clone left tree
                curr_root.left = copy_tree(root.right.left)

                # reusing - point new right to the original right subtree
                curr_root.right = root.right.right

                # curr is the cutoff whose right child will be replaced by the
                # new n
                curr = get_val_node(curr_root, node.val)

                # place n as curr right child and make curr right child as the
                # left child of n
                tmp = curr.left
                curr.left = TreeNode(num)
                curr.left.right = tmp

                next_tree.append(curr_root)
                node = node.left

        res = next_tree

for tree in generate_trees(4):
    print(tree)
