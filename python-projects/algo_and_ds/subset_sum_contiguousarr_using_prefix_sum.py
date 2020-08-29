# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

from typing import List

def is_subarray_present(arr: List[int], target: int) -> bool:
    """
    Check if any contiguous subarray sum is there matching with target
    """
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == target:
                return True
    return False

from itertools import accumulate

def s_subarray_present_better(arr: List[int], target: int) -> bool:
    """
    Check if any contiguous subarray sum is there matching with target
    """
    prefix = list(accumulate(arr))

    compl_dict = {}
    for item in prefix:
        if (item - target) in compl_dict:
            return True
        compl_dict[item] = True

    return False

print(s_subarray_present_better([1, 3, 7, -10, 4], -3))
print(s_subarray_present_better([1, 3, 7, -10, 4], 8))


"""
print "Hello, world!"

Given an array of integers and a target total X, find if there exists a contiguous subarray with sum = X

Example Test case:

Input: [1, 3, 7, -10, 4] X = -3 Output: True
           _      _
      prefix -> [1, 4, 11, 1 , 5]

      sum[:j]


                           _

                 dict = {1, 4, 11}


                 complement(complement(x)) == x


      dict - {arr[i]-x} is present or not ??

      sum between i and j

      prefix[i] - prefix[j-1]

      what's the sum of between any two indices i,j

        [-10, 1 , 3, 4 , 7]

Input: [1, 3, 7, -10, 4] X = 8 Output: False

Input: [1, 3, 7, -10, 4] X = 20 Output: False


    0    1    2    3    4    5    6    7    8
1
3
7


find the combinations of the different numbers
and then check if the sum is X
once all the combinations are checked and still you dont see X, that means that you can return false
if one of the combiantions adds up to X then you can return true

for i in index
    7
    sum = 0
    for j in all indices
        -10
        see what is the next j
        sum +=  7
        add it to my previous
        pick numbers between i and j O(n)
    reset the sum

"""
