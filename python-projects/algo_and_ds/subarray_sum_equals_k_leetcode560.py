"""

https://leetcode.com/problems/subarray-sum-equals-k/

subarray sum equals k

total number of continuous subarrays whose sum equals k

this can be done using the prefix sum as shown in the last interview

1   2   3   0   5 target = 3

1   3   6   6   11

{0, 1, 3, -3}

time: O(n)
space complexity: O(n)

"""

from itertools import accumulate
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        target = k
        prefix_sums = {0: 1}
        sum = 0
        count = 0
        for item in nums:
            sum += item
            rem = sum - target
            if rem in prefix_sums:
                count += prefix_sums[rem]
            prefix_sums[sum] = prefix_sums.get(sum, 0) + 1
            print(prefix_sums)
        return count

arr = [1,1,1]
k = 2
s = Solution()
print(s.subarraySum(arr, k))


arr = [0,0,0,0,0,0,0,0,0,0]
k = 0
s = Solution()
print(s.subarraySum(arr, k))
