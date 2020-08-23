"""
https://leetcode.com/problems/climbing-stairs/

1 -> 1
2 -> 2
3 -> 3

4 -> 7
1 1 1 1
2 1 1
1 2 1
1 1 2
2 2
3 1
1 3

5 ->
1 1 1 1 1
2 1 1 1
1 2 1 1
1 1 2 1
1 1 1 2
2 2 1
2 1 2
1 2 2
3 1 1
1 3 1
1 1 3
3 2
2 3
4 1
1 4

this looks like a simple calculation and hence can be done in O(1)

the above analysis is wrong.
i think they are expecting catalan numbers


"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)

    return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        return fibonacci(n)


s = Solution()
print(s.climbStairs(4))
