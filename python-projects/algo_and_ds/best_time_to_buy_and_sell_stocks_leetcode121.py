"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

we can probably have this as a max heap

we can then iterate over the arr
if the elem is the same as the max then remove it
else go to the next
always keep a running count of the difference between the current element and the current max

time complexity is O(nlogn)
space complexity O(n)

"""
from typing import List
from heapq import heapify, heappop

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        heap = [(-x, i) for i, x in enumerate(prices)]
        heapify(heap)
        maxvprofit = 0

        for idx, p in enumerate(prices):
            # if there are left over maxs from the previous
            # remove the earlier leftovers
            while heap and heap[0][1] < idx:
                heappop(heap)

            # now the main algo. current maxval is the max of the remaining prices
            maxval = -heap[0][0]
            maxvprofit = max(maxvprofit, maxval - p)
            if p == maxval:
                heappop(heap)
        return maxvprofit

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(prices))
