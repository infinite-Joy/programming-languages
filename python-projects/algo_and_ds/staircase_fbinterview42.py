"""
This is a fibonacci problem and using dp to solve it.

time complexity: O(n)
space: O(n) this can be reduced to O(1)

"""

#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the stepPerms function below.
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
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp)

    return dp[n]

def stepPerms(n):
    return fibonacci(n)

