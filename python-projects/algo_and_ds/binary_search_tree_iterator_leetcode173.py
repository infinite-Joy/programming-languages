"""

binary search tree iterator

https://leetcode.com/problems/binary-search-tree-iterator/

to implement the next smallest number in the tree


    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

this is basically by finding the inorder element of the tree and putting that in a list

it should use O(h)

to attain average we should have a inorder traversal
    hence we will have O(h)
    and then once it reaches the leftmost tree we will start yielding

    so basically first find the smallest element
    and then as soon as that element is reached start yielding

                1

        2               3
    4       5       6       7

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root
        yield from inorder(root.right)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = inorder(root)
        self.nextnode = None
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.nextnode:
            node = self.nextnode
            self.nextnode = None
            return node.val
        else:
            try:
                node = next(self.iterator)
                return node.val
            except StopIteration:
                return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.nextnode is None:
            try:
                node = next(self.iterator)
                self.nextnode = node
            except:
                self.nextnode = None
        return self.nextnode is not None



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
