"""
doing this using the greedy solution

go through the jump values and pick the largest val

"""

def can_jump(nums):
    curr = 0
    while curr < len(nums) - 1 and nums[curr] > 0:
        start = curr
        end = min(nums[curr] + curr, len(nums)-1)
        if end == len(nums) - 1:
            return True
        maxval = 0
        for i in range(start+1, end+1):
            maxval = max(maxval, nums[i])
            if maxval == nums[i]:
                curr = i
        print(curr)
    return curr >= len(nums) - 1

nums = [3,0,8,2,0,0,1]
nums = [4,2,0,0,1,1,4,4,4,0,4,0]
print(can_jump(nums))

# this is not working


# ======================

"""
basically i should be behind dis pointer and dis pointer should be inching closer to the finish
at some point the dis pointer will not be able to move forward.
that is when you you know that this is the end
"""

from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0
        i = 0
        while i <= dis and i < len(nums):
            dis = max(dis, i + nums[i])
            if dis >= len(nums) - 1:
                return True
            i += 1
        return False
