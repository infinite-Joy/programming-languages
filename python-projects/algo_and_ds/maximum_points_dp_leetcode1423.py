"""
we can do a recursion on the recursion tree. seems like a greedy sol can be implemented here.
so for a number we would take either one or the other
once we take it compute the curr sum and then go to the next one
1    2    3    4    5    6    1
                    *
                1        1
            3    2
    0    1    6    5
0    0    1    7    12
1    1    2    8    12
2    3    4    8    12
3    6

recorrence is T(n) = max(T(n - 1), Tn)
        T(n) = t(n) + value if the addition is less than target
from itertools import accumulate
class Solution:
def maxScore(self, cardPoints: List[int], k: int) -> int:
    dp = [0 for _ in range(k+1)]
    for i in range(1, len(k) + 1):
        dp[i] = dp[len(cardPoints) - i]
    dp = list(accumulate(dp))
    for li in range(len(k)):
        for ri in range(1, len(k) + 1):
            if li + ri >= k:
                dp[ri] = max(dp[ri], dp[ri - 1])
            else:
                dp[ri] = dp[ri] + cardPoints[li]
    return dp[k]




time complexity : O(n2)
space complexity: O(n)
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) <= k: return sum(cardPoints)
        dp = [0 for _ in range(k+1)]
        for i in range(1, k + 1):
            dp[i] = cardPoints[len(cardPoints) - i]
        dp = list(accumulate(dp))
        for li in range(k):
            for ri in range(1, k + 1):
                if li + ri >= k:
                    dp[ri] = max(dp[ri], dp[ri - 1])
                else:
                    dp[ri] = dp[ri] + cardPoints[li]
        return dp[k]
