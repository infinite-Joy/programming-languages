"""
https://leetcode.com/problems/divide-two-integers/
maybe using -
10/3
0,1,2,3,4,5,6,7,8,9 => 3 repeated 10 times
[3, 6, 9, 12, 15, .... ]
start from the middle and to towards left if more than and to wards right  if  less than and then whenever you find the range between which you get the number you return the  index + 1
===========================

time complexity: this is bst which means O(logn)
space complexity: creating a different array O(n)

"""
from itertools import accumulate
class Solution:
    def find(self, nums, dividend, start, end):
        if start + 1 == end or start == end:
            return start
        else:
            mid = (start + end) >> 1 # implementing division by 2
            if dividend < nums[mid]: # we need to go left
                return  self.find(nums, dividend, start, mid)
            elif nums[mid] < dividend: # we need to go to the right
                return self.find(nums, dividend, mid+1, end)
            else:
                return end
    def divide(self, dividend: int, divisor: int) -> int:
        """
        time complexity : lg n
        space: linear
        Args:
            dividend (int): the bigger number
            divisor (int): the smaller number
        Returns:
            int: the answer
        """
        nums = [divisor for _ in range(dividend)]
        nums = list(accumulate(nums))
        return  self.find(nums, dividend, 0, dividend)
