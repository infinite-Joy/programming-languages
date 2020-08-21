"""
segment trees

creation time complexity: O(n)

"""

from typing import List

def construct_tree(inputarr: List[int], segmenttree: List[int], low, high, pos):
    if low == high:
        segmenttree[pos] = inputarr[low]
        return

    mid = (low + high) // 2
    construct_tree(inputarr, segmenttree, low, mid, 2 * pos + 1)
    construct_tree(inputarr, segmenttree, mid+1, high, 2 * pos + 2)

    # in this case min function is being implemented. You will implement the
    # function based on the need.
    segmenttree[pos] = min(segmenttree[2*pos+1], segmenttree[2*pos+2])


from math import log
def get_next_power_2(num):
    if num & (num-1) == 0:
        return num
    digits = int(log(num, 2)) + 1
    return 1 << digits


from math import inf
arr = [-1, 2, 4, 0]
def main(arr):
    nums = get_next_power_2(len(arr))
    segmenttree_size = 2 * nums - 1
    segmenttree = [inf for _ in range(segmenttree_size)]
    construct_tree(arr, segmenttree, 0, len(arr)-1, 0)
    print(segmenttree)

main(arr)


