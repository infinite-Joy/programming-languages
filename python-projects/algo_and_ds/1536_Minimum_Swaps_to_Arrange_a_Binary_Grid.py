"""
we can probably use backtraking in this

for each backtracking we will need to create an array out of this

"""

"""
we can implement kind of a backtracking approach

with a dfs based on pruning to check if the earlier configuration has been checked dont look at it again
"""

from typing import List


def convert_to_num(row):
    num = 0
    least_set_bit = 0
    for v in range(len(row)):
        num = 2 * num + row[v]
        if row[v] == 1:
            least_set_bit = len(row) - v
    return num, least_set_bit


def


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        nums = [convert_to_num(row) for row in grid]
        count = 0
