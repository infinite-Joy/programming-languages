"""

maximum sum of 2 non overlapping arrays

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

maybe what we can do is that put things in the heap

keep an arr of 2 sum and 3 sum

    3   8   1   3   2   1   8   9   0
        11  9   4   5   3   9   17  9
            12  12  6   6   11  18  17


A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
    2   1   5   6   0   9   5   0   3   8
            8   12  11  15  14  14  8   11
                14  12

finally the maximum of the 2 values


basically
    get the left max sum , right max sum and then pick the max out of that
"""

from math import inf
from functools import reduce
from typing import List
class Solution:
    def helper(self, A, L, M):
        # l is left and m is right
        lm_prefix_arr = [-inf for _ in A]
        lm_prefix_arr[L-1] = sum(A[:L])
        for i in range(L, len(A)-M):
            outgoing = A[i - L]
            incoming = A[i]
            lm_prefix_arr[i] = lm_prefix_arr[i - 1] - outgoing + incoming
        print(lm_prefix_arr)
        max_prefix_arr = [-inf for _ in lm_prefix_arr]
        for i in range(L - 1, len(lm_prefix_arr)):
            max_prefix_arr[i] = max(max_prefix_arr[i - 1], lm_prefix_arr[i])
        print(max_prefix_arr)

        lm_suffix_arr = [-inf for _ in A]
        starting = len(A) - M
        lm_suffix_arr[starting - 1] = sum(A[starting:])
        for i in range(starting - 1, L - 1, -1):
            outgoing = A[i + M]
            incoming = A[i]
            lm_suffix_arr[i - 1] = lm_suffix_arr[i] - outgoing + incoming
        print(lm_suffix_arr)
        lm_max_suffix_arr = [-inf for _ in lm_suffix_arr]
        for i in range(len(lm_max_suffix_arr) - 2, -1, -1):
            lm_max_suffix_arr[i] = max(lm_max_suffix_arr[i + 1], lm_suffix_arr[i])
        print(lm_max_suffix_arr)

        overall_max = reduce(lambda overall_max, values: max(overall_max, sum(values)), zip(max_prefix_arr, lm_max_suffix_arr), -inf)
        print(overall_max)
        return overall_max

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        return max(self.helper(A, L, M), self.helper(A, M, L))




# test cases
A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2
sol = Solution()
print(sol.maxSumTwoNoOverlap(A, L, M))

A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
sol = Solution()
print(sol.maxSumTwoNoOverlap(A, L, M))

A = [2,1,5,6,0,9,5,0,3,8]
L = 4
M = 3
sol = Solution()
print(sol.maxSumTwoNoOverlap(A, L, M))

A = [1,0,1]
L = 1
M = 1
sol = Solution()
print(sol.maxSumTwoNoOverlap(A, L, M))
