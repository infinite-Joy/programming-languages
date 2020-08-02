# -*- coding: utf-8 -*-

"""
move zeros to the end challenge on pramp
what can be done is that we will two pointers, similar to the sliding window
i will be the start of the 0’s
and j will be the current.

there  will be a running counter of j
whenever j is not 0, then swap with i, update i  and update j
if j is 0 then just update j
================================
"""


def find_first_zero(arr):
    for i, el in enumerate(arr):
        if el == 0:
            return  i


def move_zeros(arr):
    i = find_first_zero(arr)
    if i is None:
        return arr
    j = 0
    while j < len(arr):
        print(i, j, arr)
        chi = arr[i]
        chj = arr[j]
        if i < j  and chj != 0:
            print('swap', i, j)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr

print(move_zeros([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
