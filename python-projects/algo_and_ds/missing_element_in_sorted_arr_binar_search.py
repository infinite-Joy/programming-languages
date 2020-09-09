"""

missign element in a sorted arr

leetcode 1060

to do this we will start from teh first element and then add k to it
next we will loop over the remaining element and see if the elem is within the value then incr val
if element greater than val or elem is done then return the val

time complexity: O(min(k or size of nums))

this can also be done using binary search

    missing = nums[0] + k
    if missing more than the last element or equal:
        return missing + size of the arr - 1

    else: binary search
        middle element = 7, missing = 7
        if middle element less
            update val = val + index - 1
            low = mid + 1
        if middle element more

"""

from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = nums[0] + k
        if missing >= nums[-1]:
            return missing + len(nums) - 1

        # implement binary search in the other case
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= missing:
                missing += mid
                low = mid + 1
            else:
                high = mid
        return missing

# test cases
A = [4,7,9,10]
K = 1
# Output: 5
sol = Solution()
print(sol.missingElement(A, K))

Input: A = [4,7,9,10]
K = 3
#Output: 8
sol = Solution()
print(sol.missingElement(A, K))

this is not exactly working. need to see the actual solution
