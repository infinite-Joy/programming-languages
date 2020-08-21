"""

https://leetcode.com/problems/search-in-rotated-sorted-array/

this can probably be done in a binary search manner.

first we need to ffind the pivot,
    if left > right:
        shift right
    else
        shigt left

once the pivot is found then divide into two arrays.
    and then do the finding the in the two arrays

so complexity is O(log n)

[4,5,6,7,0,1,2]
       i j
max = i
min = j

leftmin = 0
leftmax = max

rightmin = j
rightmax = n

range = rightmin, rightmax

do binary search within that range
"""

from typing import List

def bin_search_pivot(arr, left, right):
    if left == right:
        return left
    mid = (left+right) // 2
    if arr[left] >= arr[mid]:
        return bin_search_pivot(arr, left, mid)
    else:
        return bin_search_pivot(arr, mid, right)

def bin_search(arr, low, high, target):
    if low == high:
        if arr[low] == target:
            return low
        else:
            return -1
    mid = (low+high) // 2
    if target <= arr[mid]:
        return bin_search(arr, low, mid, target)
    else:
        return bin_search(arr, mid+1, high, target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        pivot = bin_search_pivot(nums, 0, len(nums)-1)
        maxval = nums[pivot]
        minval = nums[pivot+1]

        # if target is outside the range
        if target < minval or target > maxval:
            return -1

        if target >= nums[0]:
            # target is in the left part
            return bin_search(nums, 0, pivot, target)
        else:
            # target is in the right part
            return bin_search(nums, pivot+1, len(nums)-1, target)


s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums, target))

nums = [1]
target = 0
print(s.search(nums, target))
