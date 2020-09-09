"""

missign element in a sorted arr

leetcode 1060

to do this we will start from teh first element and then add k to it
next we will loop over the remaining element and see if the elem is within the value then incr val
if element greater than val or elem is done then return the val

time complexity: O(min(k or size of nums))

"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        val = nums[0] + k
        for i in range(1, len(nums)):
            elem = nums[i]
            if elem <= val:
                val += 1
            else:
                return val
        return val
