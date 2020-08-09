"""
https://leetcode.com/contest/weekly-contest-201/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
Given an array nums and an integer target.
Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.
This looks like a two pointer thing to me.
but i will need to sort the array first
this looks like a dp solution to me.
[-1,3,5,1,4,2,-9]
[-2,6,6,3,5,4,1,2,8]
[-2, ]

    -2    -1    2    3    4    5    6    7    8    9    10    11 12
0    1    0    0    0    0    0    0    0    0    0    0    0  0
8    1    0    0    0    0    0    0    0    1    0    0    0  0
8    1    0    0    0    0    0    0    0    2    0    0    0  0
5    1    0    0    0    0    1    0    0    2    0    0    0  0
7    1    0    0    0    0    1    0    1    2    0    0    0  1
6    1    0    0    0    0    1    1    0    2    0    0    1  1
3    1    0    0    1    0    1    1    4    2    1    1    2  1
4    1    1    0    1    1    2    2    2    3    1    1    1  1
10    1    1    0    1    1    2    2    2    3    1    2    1

f negative numbers are there convert them all to positive numbers
then what you can do is implement dp for the coin change without replacement problem
this is not working out.
try something else
[-1,3,5,1,4,2,-9]
i = 0, j = 1 => 2
i = 1 j = 2 => 8
i = 1, j = 3 => 9
i = 2, j = 3 => 6 match
i = 4, j = 5 => 6 match
==============
    -2    6    6    3    5    4    1    2    8
    _    _ => 8
    _        _ => 14
        _    _ => 12
            _    _ => 9
            _        _ => 14
                _    _ => 8
                _        _ => 12
                    _    _ => 9
                    _        _ => 10 match

time complexity O(n)
space complexity O(1)
"""

def main(nums, target):
    print(nums)
    i = 0
    j = 0
    matches = 0
    sum = 0
    while j < len(nums):
        print(i, j, matches, sum)
        if sum == target:
            matches += 1
            sum = 0
        if j < len(nums) and i == j:
            sum = nums[i]
            if sum == target:
                matches += 1
                i += 1
                j = i
                sum = nums[i]
            else:
                j += 1
                sum = sum + nums[j]
        elif nums[i] + nums[j] == target:
            matches += 1
            j += 1
            i = j
            sum = nums[i]
        elif nums[i] + nums[j] < target:
            j += 1
            sum = sum + nums[j]
        else: #elif nums[i] + nums[j] > target:
            val = nums[i]
            i += 1
            sum = sum - val
    return matches


nums = [1,1,1,1,1]
target = 2
print(main(nums, target))

nums = [-1,3,5,1,4,2,-9]
target = 6
print(main(nums, target))







