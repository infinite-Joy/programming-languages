"""

maximum subarray using prefix sum

nums = [-2, 1,  -3, 4,  -1, 2,  1,  -5, 4]

this is probably using kadanes algo

        0  1  0  4   3   5   6   1   5
        -2



"""

from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol_mixed_arr = 0
        curr_subarr_sum = 0
        sol_negative_arr = -inf
        mixedarr = False

        for item in nums:
            if item > 0:
                mixedarr = True
            if mixedarr is False:
                sol_negative_arr = max(sol_negative_arr, item)

            # processing for elements that contains both elements
            curr_subarr_sum = max(curr_subarr_sum + item, 0)
            sol_mixed_arr = max(sol_mixed_arr, curr_subarr_sum)

        if mixedarr is True:
            return sol_mixed_arr
        return sol_negative_arr


