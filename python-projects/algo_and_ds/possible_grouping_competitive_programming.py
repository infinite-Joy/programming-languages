#An illustration: UVa Online Judge [47] Problem Number 10911 (Forming Quiz Teams).
# to get this take one reference and then sort the values
# {1,1},{8,6},{6,8},and{1,3}
# 2 14 14 4
# 2, 4, 14, 14
# root(8) + root(8)

# time complexity: O(nlgn)
# space complexity: O(n)

from math import sqrt

def find_cost(pairs):
    total_cost = 0
    for (x1, y1), (x2, y2) in pairs:
        total_cost += sqrt((x2-x1)**2 + (y2-y1)**2)
    return total_cost

def cost(arr):
    values = [(i, x+y) for i, (x, y) in enumerate(arr)]
    values = sorted(values, key=lambda x: x[1])

    no_vals = len(values) // 2
    pairs = [(arr[values[2*i][0]], arr[values[2*i+1][0]]) for i in range(no_vals)]

    return find_cost(pairs)

print(cost([[1,1], [8,6], [6,8], [1,3]]))
