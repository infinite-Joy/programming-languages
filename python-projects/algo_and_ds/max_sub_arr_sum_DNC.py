"""

maximum subarray using prefix sum

nums = [-2, 1,  -3, 4,  -1, 2,  1,  -5, 4]

this is probably using kadanes algo

        -2      1      -3      4        -1      2       1       -5      4

divide and conquer approach

    select the middle element, the answer may contain the middle element or may not contain the middle element
    if it does not contain the middle element go to the left and right and find the max of left and right
    if it contains the middle element get the max prefix sum and the max suffix sum and then add the result
    return the max of the three




"""

from math import inf
from typing import List
class Solution:
    def find_max_crossing_subarr(self, nums, low, high, mid):
        leftsum = -inf
        sum = 0
        maxleft = mid
        for i in range(mid, low-1, -1):
            sum = sum + nums[i]
            if sum > leftsum:
                leftsum = sum
                maxleft = i
        rightsum = -inf
        sum = 0
        maxright = mid + 1
        for i in range(mid + 1, high + 1):
            sum = sum + nums[i]
            if sum > rightsum:
                rightsum = sum
                maxright = i
        return maxleft, maxright, leftsum + rightsum

    def divide_and_conquer(self, nums, start, end):
        import time; time.sleep(1)
        print(nums, start, end)
        if start == end:
            return start, end, nums[start]
        mid = (start + end) // 2
        leftlow, lefthigh, leftsum = self.divide_and_conquer(nums, start, mid)
        rightlow, righthigh, rightsum = self.divide_and_conquer(nums, mid + 1, end)
        crosslow, crosshigh, crosssum = self.find_max_crossing_subarr(nums, start, end, mid)
        print(crosslow, crosshigh, crosssum)

        maxsum = max(leftsum, rightsum, crosssum)
        if maxsum == leftsum:
            return leftlow, lefthigh, leftsum
        if maxsum == rightsum:
            return rightlow, righthigh, rightsum
        return crosslow, crosshigh, crosssum

    def maxSubArray(self, nums: List[int]) -> int:
        _, _, maxsum = self.divide_and_conquer(nums, 0, len(nums) - 1)
        return maxsum

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-2,1,-3]
sol = Solution()
print(sol.maxSubArray(nums))

# solution taken from CLRS book

nums = [1,2]
sol = Solution()
print(sol.maxSubArray(nums))
