"""
merge intervals

https://leetcode.com/problems/merge-intervals/discuss/355318/Fully-Explained-and-Clean-Interval-Tree-for-Facebook-Follow-Up-No-Sorting

merge intervals using interval tree

this is also nlogn uses additional tree

advantage is that this can work on a stream and will probably not grow as high as the stream

"""

from typing import List

class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.left = self.right = None

class Solution:
    def add(self, root, interval):
        start, end = interval
        node = root

        while node:
            if node.start <= start <= node.end:
                node.end = max(node.end, end)
                return
            elif node.start <= end <= node.end:
                node.start = min(node.start, start)
                return
            else:
                if start <= node.mid:
                    if node.left is None:
                        new_node = TreeNode(start, end)
                        node.left = new_node
                        node = None
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        new_node = TreeNode(start, end)
                        node.right = new_node
                        node = None
                    else:
                        node = node.right
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # define the root
        root = TreeNode(*intervals[0])

        for interval in intervals:
            self.add(root, interval)

        return [[node.start, node.end] for node in self.inorder(root)]


# test case
intervals = [[1,4],[4,5]]
s = Solution()
print(s.merge(intervals))


intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))

"""

another implementation is using the geeks for geeks method

https://www.geeksforgeeks.org/interval-tree/

"""

from collections import namedtuple

class TreeNode:
    def __init__(self, start, end, max):
        self.start = start
        self.end = end
        self.max = max
        self.left = self.right = None

class Solution:
    def add(self, interval, root=None):
        start, end = interval
        if root is None:
            root = TreeNode(start, end)

        # if the roots value is smaller than new interval goes to the left
        if start < root.start:
            root.left = self.add(interval, root.left)

        else:
            root.right = self.add(interval, root.right)

        # update the max value of this ancestor if needed
        root.max = max(root.max, interval[1])

        return root
    def is_overlap(self, interval1, interval2):
        if interval1 > interval2:
            interval1, interval2 = interval2, interval1
        right_of_left = interval1[1]
        left_of_right = interval2[0]
        return right_of_left >= left_of_right
    def overlap_search(self, root, interval):
        # base case tree is empty
        if root:

            # if the interval overlaps with the root interval
            if self.is_overlap([root.start, root.end], interval):
                return [root.start, root.end]

            # if left child of root is present and max of left child is greater
            # than or equal to the given interval, then it may overlap with an interval
            # in left subtree
            if root.left and root.left.max >= start:
                return self.overlap_search(root.left, interval)

            # interval can only overlap with right subtree
            return self.overlap_search(root.right, interval)

    def inorder(self, root):
        if root:
            yield from inorder(root.left)
            yield root
            yield from inorder(root.right)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # this is not done and shou;d be explored next
        if not intervals:
            return []

        for interval in intervals:
            self.add(interval)

        return [[node.start, node.end] for node in self.inorder(root)]


