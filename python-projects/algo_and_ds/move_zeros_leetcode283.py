"""

https://leetcode.com/problems/move-zeroes/

move zeros to the end can probably be done using 2 pointer method

[0,1,0,3,12]
 _ _

 check i and j

 if i is 0 and j is not 0: swap; incr i incr j
 if i is not 0: incr i, if j < i; j = i + 1
 else; incr i incr j

 time complexity: O(n) since using 2 pointer
 space complexity: O(1)

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
                if j <= i:
                    j = i + 1
