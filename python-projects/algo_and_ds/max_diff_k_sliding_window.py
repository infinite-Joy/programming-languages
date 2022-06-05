"""
nums = [3,6,1,2,5], k = 2
nums = 1,2,3,5,6

complexity O(n log n)

also having a sliding window approach on top of it


"""


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        count = 1
        i = 0
        j = i
        l = len(nums)
        while i < l and j < l:
            if nums[j] - nums[i] <= k:
                j += 1
            else:
                i = j
                count += 1
        return count