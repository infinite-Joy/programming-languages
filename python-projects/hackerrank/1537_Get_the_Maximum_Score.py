"""
 1537. Get the Maximum Score

https://leetcode.com/contest/weekly-contest-200/problems/get-the-maximum-score/

using two pointers and then doing dp

Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].

"""

from typing import List

def find_dups(nums1, nums2):
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            yield i, j
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1


def break_arrs(nums1, nums2):
    sums1, sums2 = [], []
    s1, s2 = 0, 0
    for bp1, bp2 in find_dups(nums1, nums2):
        print('dups', bp1, bp2)
        sum1 = sum(nums1[s1:bp1])
        sum2 = sum(nums2[s2:bp2])
        yield sum1, sum2
        s1, s2 = bp1, bp2
    yield sum(nums1[s1:len(nums1)]), sum(nums2[s2:len(nums2)])


def bigger_path_traversal(arr1, arr2):
    maxsum = 0
    for p1, p2 in break_arrs(arr1, arr2):
        print(maxsum, p1, p2)
        maxsum = maxsum + max(p1, p2)
    return maxsum


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        return bigger_path_traversal(nums1, nums2)

s = Solution()
nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]
print(nums1, nums2)
print(s.maxSum(nums1, nums2))

