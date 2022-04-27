"""
one way is to do like a partition

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

merging of two sorted arrays can be done in O(n) time.

but this is more work than required.

two single arrays
1 and empty => same
1   2 => middle of the two
1   3 =, 2 4


1   2   3   4   5   6   7
            ^

[1  3   5   7] [2   4   6] total = 7, - 2, 3.5, 3, 4, 1

[1  2   3   4][5    6   7] => 2, 2.5 2 ; 1, 6, 1
[3  4][5    6]
[4][5]

if right higest is less than left lowest or vice versa then its fine

take median of one. search in the other.
find the place of 


"""

def get_median1(arr1, arr2):
    # brute force
    total = sorted(arr1, arr2)
    size = len(total)
    if size % 2 == 1:
        mid = int(size / 2)
        return total[mid]
    else:
        mid = int(size / 2)
        return (total[mid-1] + total(mid))/2



def merge(arr1, arr2):
    left = 0
    right = 0
    new = []
    while left < len(arr1) and right < len(arr2):
        left_val = arr1[left]
        right_val = arr2[right]
        if left_val <= right_val:
            new.append(left_val)
            left += 1
        else:
            new.append(right_val)
            right += 1
    new.extend(arr1[left:])
    new.extend(arr2[right:])
    return new

def get_median2(arr1, arr2):
    # brute force
    total = merge(arr1, arr2)
    size = len(total)
    if size % 2 == 1:
        mid = int(size / 2)
        return total[mid]
    else:
        mid = int(size / 2)
        return (total[mid-1] + total[mid])/2


1   2   3   4   5   6   7   
1   2   3   4   5

def validity(arr1, arr2, left_arr1, left_arr2, elem_on_left):
    if left_arr1 + left_arr2 == elem_on_left:
        if arr1[left_arr1-1] < arr2[left_arr2] and arr2[left_arr2-1] < arr1[left_arr1]:
            return True
    return False


def get_median3(arr1, arr2):
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    elem_on_left = int((len(arr1) + len(arr2)) / 2) # elements
    left_arr2 = 0
    left_arr1 = 0
    l = 0
    r = len(arr2) - 1
    # while validity(arr1, arr2, left_arr1, left_arr2, elem_on_left) is False:
    while True:
        left_arr2 = int(len(arr2) / 2)
        left_arr1 = elem_on_left - left_arr2



nums1 = [1,3]
nums2 = [2]
print(get_median2(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(get_median2(nums1, nums2))