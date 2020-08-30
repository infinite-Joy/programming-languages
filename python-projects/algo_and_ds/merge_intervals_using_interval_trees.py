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
