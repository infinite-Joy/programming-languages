from math import log2
from bisect import bisect_left, bisect_right

def get_bounds(n):
    right = 1
    while n > (2 ** right):
        right += 1
    return right

@profile
def log2_custom(n, precision=100_000_000):
    if n == 1:
        return 0

    right = get_bounds(n)
    nums = [x/precision for x in range(precision*(right-1), precision*right)]

    # # only supporting from python3.10
    output = bisect_left(nums, n, key=lambda x: 2 ** x)
    print(log2(n))
    return nums[output-1]

n = 18
print(log2_custom(n))
print(log2(n))