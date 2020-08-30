"""

longest continuous increasing subsequuence

we can use the 2 pointer method

Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.



"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        i = 0
        j = 1
        maxval = 0
        while j < len(nums):
            if nums[j] > nums[i]:
                j += 1
            else:
                i = j
                j += 1
            maxval = max(maxval, j - i)
        return maxval


