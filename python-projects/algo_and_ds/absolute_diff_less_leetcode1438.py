"""

i am thinking that a 2 pointer may work in this case

    8   2   4   7
            _
                _
                5

    10  1   2   4   7   2       target 5
            _
                        _

i think a 2 pointer solution would work here
absolute diff less than limit

keep on moving the 2 pointer,
update the max val and the min val
if the diff > target decrease the slider
if the diff < target update the max elements

since we are now working with heaps this is nlogn

"""
from typing import List
from math import inf
from heapq import heappush, heappop
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums: return 0
        max_size = 0
        left_pointer = 0
        right_pointer = 0
        curr_min = nums[0]
        curr_max = nums[0]
        minheap = [nums[0]]
        max_heap = [-curr_max]
        while right_pointer < len(nums):
            diff = curr_max - curr_min
            if diff > limit:
                outgoing = nums[left_pointer]
                if outgoing == curr_min:
                    heappop(minheap)
                    curr_min = minheap[0]
                if outgoing ==  curr_max:
                    heappop(max_heap)
                    curr_max = -max_heap[0]
                left_pointer += 1
            else: # diff is less than or equal to the limit we increase the window size
                max_size = max(max_size, right_pointer - left_pointer + 1)
                right_pointer += 1
                if right_pointer < len(nums):
                    incoming = nums[right_pointer]
                    heappush(minheap, incoming)
                    heappush(max_heap, -incoming)
                    curr_min = minheap[0]
                    curr_max = -max_heap[0]
        return max_size

# test case
nums = [8,2,4,7]
limit = 4
sol = Solution()
print(sol.longestSubarray(nums, limit))

nums = [10,1,2,4,7,2]
limit = 5
sol = Solution()
print(sol.longestSubarray(nums, limit))

nums = [4,2,2,2,4,4,2,2]
limit = 0
sol = Solution()
print(sol.longestSubarray(nums, limit))
