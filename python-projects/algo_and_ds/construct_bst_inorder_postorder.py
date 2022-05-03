"""



"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return " ".join([str(self.val), self.left.__repr__(), self.right.__repr__()])


def get_root_from_postorder(inorder, postorder, initstart, initend, postorder_indx):
    rootval = inorder[0]
    max_pos = 0
    inorder_pos = 0
    for i in range(initstart, initend+1):
        elem = inorder[i]
        max_pos = max(max_pos, postorder_indx[elem])
        if max_pos == postorder_indx[elem]:
            inorder_pos = i
    return inorder[inorder_pos], inorder_pos

def build_tree(inorder, postorder, initstart, initend, postorder_indx):
    if initstart <= initend:
        print(initstart, initend)
        rootval, inorder_pos = get_root_from_postorder(
            inorder, postorder, initstart, initend, postorder_indx)
        print('rootval, inorder_pos', rootval, inorder_pos)
        root = TreeNode(rootval)
        root.left = build_tree(inorder, postorder, initstart, inorder_pos-1, postorder_indx)
        root.right = build_tree(inorder, postorder, inorder_pos+1, initend, postorder_indx)
        return root

def main(inorder, postorder):
    if inorder:
        initstart, initend = 0, len(inorder)-1 # 0, 0
        postorder_indx = {n: i for i, n in enumerate(postorder)} # {-1:0}
        print(postorder_indx)
        root = build_tree(inorder, postorder, initstart, initend, postorder_indx)
        return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = main(inorder, postorder)
print(root.val)
print(root.left.val)
print(root.right.val)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

inorder : left, root, right
post order left, right, root

probably using a queue.
since this is a binary tree, we need to take care of things 3 at a time

inorder means that left, root, right.

so from postorder get the root. then divide inorder to left, root, right
take right, from post order get the root, divide inorder to left root, right

time complexity: O(n2) becuase each elem will be traversed at most 2n times.
space complexity: O(n)


"""

import math


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def get_root_from_postorder(inorder, postorder, initstart, initend, postorder_indx):
            rootval = inorder[0]
            max_pos = 0
            inorder_pos = 0
            for i in range(initstart, initend+1):
                elem = inorder[i]
                max_pos = max(max_pos, postorder_indx[elem])
                if max_pos == postorder_indx[elem]:
                    inorder_pos = i
            return inorder[inorder_pos], inorder_pos
        
        def build_tree(inorder, postorder, initstart, initend, postorder_indx):
            if initstart <= initend:
                rootval, inorder_pos = get_root_from_postorder(
                    inorder, postorder, initstart, initend, postorder_indx)
                root = TreeNode(rootval)
                root.left = build_tree(inorder, postorder, initstart, inorder_pos-1, postorder_indx)
                root.right = build_tree(inorder, postorder, inorder_pos+1, initend, postorder_indx)
                return root
        
        def main(inorder, postorder):
            if inorder:
                initstart, initend = 0, len(inorder)-1 # 0, 0
                postorder_indx = {n: i for i, n in enumerate(postorder)} # {-1:0}
                root = build_tree(inorder, postorder, initstart, initend, postorder_indx)
                return root
            
        return main(inorder, postorder)

"""
this works but we can do better
"""