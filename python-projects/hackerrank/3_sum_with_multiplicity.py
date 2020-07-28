"""
Solving using dp

solution is in O(n*target) complexity
and space complexity is O(target)

so if target < n then use this else use the simple solution
"""

from typing import List
from pprint import pprint


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        dp = [[0 for _ in range(3+1)] for _ in range(target+1)]
        dp[0][0] = 1
        for j in range(len(A)):
            for i in range(target, A[j]-1, -1):
                for k in range(3, 0, -1):
                    dp[j][k] += dp[i - A[j]][k-1]

            print(i, j, A)
            pprint(dp)
            __import__('pdb').set_trace()

s = Solution()
A = [1,1,2,2,3,3,4,4,5,5]
target = 8
s.threeSumMulti(A, target)

