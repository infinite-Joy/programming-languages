"""
https://leetcode.com/problems/next-permutation/

start: Sun Apr 10 21:46:27 IST 2022
Sun Apr 10 22:05:30 IST 2022

naive solution is to find all the combinations and then sort them

strategy. keep going till you get the first non increasing val. then swap them

ex: 151 > 511

cases:
    all monotonically increasing
        go to the last and then swap

    all monotonically decreasing
        321 > 

    cycles, increasing, decreasing cycles.

    # lst = [1, 5, 10, 9, 8, 3, 4]
# lst = [1, 5, 10, 9, 8, 6] > (1, 6, 5, 8, 9, 10)
# lst = [1, 5, 10, 9, 8, 4]
# lst = [1, 5, 10, 9, 8]

this does not seem to have any pattern

"""

import itertools

# lst = [1, 5, 10, 9, 8, 3, 4]
# lst = [1, 5, 10, 9, 8, 6] > (1, 6, 5, 8, 9, 10)
# lst = [1, 5, 10, 9, 8, 4]
# lst = [1, 5, 10, 9, 8]

# print(sorted(list(itertools.permutations(lst)))) # so basically finding this was correct.


# https://www.youtube.com/watch?v=6qXO72FkqwM

import math

def all_descending(lst): # O(n)
    prev = math.inf
    for item in lst:
        if prev >= item:
            prev = item
        else:
            return lst, False
    for i in range(int(len(lst)/2)):
        lst[i], lst[(len(lst)-1-i)] = lst[(len(lst)-1-i)], lst[i]
    return lst, True

def all_ascending(lst):
    prev = 0
    for item in lst:
        if prev <= item:
            prev = item
        else:
            return lst, False
    lst[-2], lst[-1] = lst[-1], lst[-2]
    return lst, True


def get_first_elem_for_swapping(lst):
    next = 0
    for i in range(len(lst)-1, -1, -1): # start from the last
        item = lst[i]
        if item < next: # peak is cross, hence swap
            return lst, i
        else:
            next = item
    return lst, i

def get_sec_elem_for_swapping(lst, first_index):
    left_elem = lst[first_index]
    for i in range(first_index+1, len(lst)): # now go towards the right to get the second highest element
        right_elem = lst[i]
        if right_elem <= left_elem: # peak is cross, hence swap
            return lst, i - 1 # return the previous elem to the elemen where the switch happened,
    return lst, i

def find_and_swap(lst):
    lst, first_index = get_first_elem_for_swapping(lst)
    # print(lst, first_index)
    lst, sec_index = get_sec_elem_for_swapping(lst, first_index)
    # print(lst, sec_index)
    lst[first_index], lst[sec_index] = lst[sec_index], lst[first_index]
    return lst, first_index


def gen_case(lst):
    lst, i = find_and_swap(lst)
    sorted_rem = sorted(lst[i+1:]) # sort the remaining items to get the lowest value of the remaining numbers
    for j, elem in zip(range(i+1, len(lst)), sorted_rem): # this weird thing because we need in place change
        lst[j] = elem
    return lst


def get_next_permutation(lst):
    if len(lst) == 0:
        return lst

    # special case 1: only one element
    if len(lst) == 1:
        return lst

    # all descending
    all_descending_special_case = all_descending(lst)
    if all_descending_special_case[1]:
        return all_descending_special_case[0]

    # all ascending
    all_asc = all_ascending(lst)
    if all_asc[1]:
        return all_asc[0] 

    # general case
    return gen_case(lst)


# lst = [4,3,2,1]
# print(lst, '>', get_next_permutation(lst))
# print(get_next_permutation([1,2,3,4]))
# print(get_next_permutation([1, 5, 10, 9, 8, 4]))

# # ====================
# print("#" * 20)
# lst = [1, 3, 2]
# print(lst)
# print('get_next_permutation', get_next_permutation(lst)) # 213
# print(lst)

print("#" * 20)
lst = [1, 5, 1]
print(lst)
print('get_next_permutation', get_next_permutation(lst)) # 511
print(lst)