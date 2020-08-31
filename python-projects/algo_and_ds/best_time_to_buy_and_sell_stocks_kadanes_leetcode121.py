"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

another way of doing this is using the kadanes algorithm

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

7   1   5   3   6   4
    _

min val = 1
max diff = 0

1, 4
1, 2
1, 5
1, 3


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

7, 0
6, 0
4, 0


looks like we can use the kadanes algo

if kadanes work then we will be able to do this in O(n)

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        minval = prices[0]
        maxdiff = 0

        for p in prices[1:]:
            # we have found the min val and we will update it
            minval = min(minval, p)

            # now we update the max diff seen so far
            maxdiff = max(maxdiff, p - minval)

        return maxdiff

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))

prices = [7,6,4,3,1]
s = Solution()
print(s.maxProfit(prices))
