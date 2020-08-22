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

def bin_search_pivot(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left+right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left

def bin_search(arr, low, high, target):
    if low == high:
        if arr[low] == target:
            return low
        else:
            return -1

    while low <= high:
        mid = (low+high) // 2
        if target <= arr[mid]:
            high = mid
        else:
            low = mid

    return low


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # is the index of the smallest value and also the number of places
        # rotated.
        pivot = bin_search_pivot(nums)

        print('pivot', pivot)
        maxval = nums[pivot-1]
        minval = nums[(pivot+1)%len(nums)]

        # if target is outside the range
        if target < minval or target > maxval:
            return -1

        if target >= nums[0]:
            # target is in the left part
            return bin_search(nums, 0, pivot-1, target)
        else:
            # target is in the right part
            return bin_search(nums, pivot, len(nums)-1, target)


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

nums = [1, 3]
target = 1
print(s.search(nums, target))
