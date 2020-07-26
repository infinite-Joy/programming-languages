import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*x for x in nums]
        heapq.heapify(nums)
        sol = None
        count = 0
        while nums and count <k:
            print(nums, count)
            sol = heapq.heappop(nums)
            count += 1
        if sol is not None:
            return -1*sol


s = Solution()

#print(s.findKthLargest([3,2,1,5,6,4],2))
print(s.findKthLargest([-1, 2, 0], 2))
