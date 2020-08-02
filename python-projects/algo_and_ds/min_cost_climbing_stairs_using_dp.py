"""
dynamic programming

solution in O(n)

mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))

"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        front_1 = 0
        front_2 = 0
        current_cost = 0
        for c in cost[::-1]:
            print(front_1, front_2, c, current_cost)
            current_cost = c + min(front_1, front_2)
            front_2 = front_1
            front_1 = current_cost
        return min(front_1, front_2)

s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
