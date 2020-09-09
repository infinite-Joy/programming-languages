"""

time needed to inform all employees

leetcode 1376

so first we will build the tree

and then do a bfs on it. if the next.next is not none then only add that to the queue

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.emp = []

from collections import deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [TreeNode(informTime[i]) for i in range(n)]
        head = nodes[headID]

        # do the connection
        for i, m in enumerate(manager):
            if m != -1:
                nodes[m].emp.append(nodes[i])

        # do the bfs
        time = 0
        queue = deque([(head, time)])
        while queue:
            manager, time = queue.popleft()
            print(manager, time)
            for child in manager.emp:
                queue.append((child, time + manager.val))
        return time

# test cases
n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
sol = Solution()
print(sol.numOfMinutes(n, headID, manager, informTime))

n = 7
headID = 6
manager = [1,2,3,4,5,6,-1]
informTime = [0,6,5,4,3,2,1]
sol = Solution()
print(sol.numOfMinutes(n, headID, manager, informTime))

we can use path compression as well
