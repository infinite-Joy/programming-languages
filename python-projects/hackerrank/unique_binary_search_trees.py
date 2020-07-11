from typing import List
from itertools import permutations
from collections import deque
from functools import lru_cache


class TreeNode:
    """A BST tree"""
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
        self.count  = 0

    def find_parent(self, val, root):
        if val == root.val:
            return None, None # value present in the tree
        elif val < root.val:
            if root.left is None:
                return  root, 'L'
            else:
                return self.find_parent(val, root.left)
        else:
            if root.right is None:
                return root, 'R'
            else:
                return self.find_parent(val, root.right)

    def add(self, elem):
        parent, dir = self.find_parent(elem, self.root)
        if parent is not None:
            node = TreeNode(elem)
            if dir == 'L':
                parent.left = node
            elif dir == 'R':
                parent.right = node

    def create_tree(self, elements):
        for i, elem in enumerate(elements):
            if i == 0:
                self.root = TreeNode(elem)
            else:
                self.add(elem)
        self

    def bfs(self):
        queue = deque([self.root])
        nodes = []
        while queue:
            node = queue.popleft()
            if node is None:
                nodes.append(None)
            else:
                nodes.append(node.val)
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        return nodes

    def __eq__(self, other):
        if self.bfs() == other.bfs():
            return True
        else:
            return  False

    def inorder_traversal(self, root):
        if root.left is not None:
            yield from self.inorder_traversal(root.left)
        yield root.val
        if root.right is not None:
            yield from self.inorder_traversal(root.right)

    def __iter__(self):
        yield from self.inorder_traversal(self.root)

    def __repr__(self):
        return " ".join(map(lambda x: str(x), self.__iter__()))


class Solution:
    @staticmethod
    def generateTrees(n: int) -> List[TreeNode]:
        solution = []
        for combination in permutations(range(1, n+1), n):
            print(combination)
            bst = BST()
            bst.create_tree(combination)
            solution.append(bst)
        print(solution)
        solution = [x.bfs() for x in solution]
        for x in solution:
            while x and x[-1] is None:
                x.pop()
        print(solution)
        solution = [tuple(s) for s in solution]
        solution = set(solution)
        return [list(s) for s in solution]


print(Solution.generateTrees(3))
