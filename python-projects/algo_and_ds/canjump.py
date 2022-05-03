"""
hi are you there?
did you connect?

currently I am thinking using brute force as this 
and then we can work towards memoising this.
because this is a problem with problems composing of smaller problems.

this is a graph problem.

complexity is linear as there are a linear number of nodes here.
"""


# class Solution:
# 	# @param A : list of integers
# 	# @return an integer
# 	def canJump(self, A):
	    
# 	    def dfs(arr, start):
# 	        if start == end:
# 	            return True
#             for jump in range(1, arr[start]+1):

from collections import deque

def canJump(nums) -> bool:
    arr = nums
    curr = 0
    queue = deque([0])
    target = len(nums) - 1
    visited = [False for _ in nums]
    visited[0] = True
    while queue:
        curr = queue.popleft()
        print(curr, arr[curr])
        if curr == target:
            return True
        for jump in range(1, arr[curr]+1):
            next_val = curr + jump
            if next_val < len(arr) and visited[next_val] is False:
                queue.append(next_val)
                visited[next_val] = True
            next_val = curr - jump
            if next_val > 0 and visited[next_val] is False:
                queue.append(next_val)
                visited[next_val] = True
    return False

nums = [2,3,1,1,4]
print(nums)
print(canJump(nums))