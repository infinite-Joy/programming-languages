"""
Finding the catalan numbers
"""

# the numbers can be done using the catalan numbers
# but the actual values needs to be done using backtracking.

def catalan(n):
    # reference http://www.geometer.org/mathcircles/catalan.pdf
    if n == 0 or n == 1:
        return 1

    # Table to store results of subproblems
    dp = [0 for _ in range(n+1)]

    # initialise the first two values of the table
    dp[0] = 1
    dp[1] = 1

    # fill entries using the recursive formula
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
            print(i, j, dp[i])
        print(dp)

    return dp[n]

print(catalan(3))



