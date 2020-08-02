# based on the problem https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
import math

def power_sum(X, N, num):
    if math.pow(num, N)<X:
        return power_sum(X, N, num+1) + power_sum(X-math.pow(num, N), N, num+1)
    elif math.pow(num, N) == X:
        return 1
    else:
        return 0


print(power_sum(100, 2, 1))
