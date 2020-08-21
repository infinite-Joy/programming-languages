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
    return segmenttree

segmenttree = main(arr)

# now how to do a range query on  the segment tree

def range_min_query(segmenttree: List[int], query_low: int, query_high: int, low: int, high: int, pos: int) -> int:
    """
    time complexity of this range query is O(logn)
    """
    print(segmenttree, query_low, query_high, low, high, pos)
    if query_low <= low and query_high >= high: # total overlap
        return segmenttree[pos]
    if query_low > high or query_high < low: # no overlap
        return inf
    mid = (low+high)//2
    return min(
        range_min_query(segmenttree, query_low, query_high, low, mid, 2*pos+1),
        range_min_query(segmenttree, query_low, query_high, mid+1, high, 2*pos+2),
    )

range_min = range_min_query(segmenttree, 1, 3, 0, len(arr)-1, 0)
print(range_min)



