"""
implementation using heaps

done in O(logk) approach

"""

from heapq import heappush, heappop

def merge_k_lists(lists):
    heap = []
    # take atleast one element from all the lists
    for i, onelist in enumerate(lists):
        if onelist:
            heappush(heap, (onelist[0], i, 0))
    # print(heap)
    mergedlist = []
    while heap:
        elem, i, j = heappop(heap)
        # print(elem)
        mergedlist.append(elem)
        # print(mergedlist)
        if j+1 < len(lists[i]):
            j += 1
            heappush(heap, (lists[i][j], i, j))
    return mergedlist


lists = [[1,4,5],[1,3,4],[2,6]]
print('original list', lists)
print(merge_k_lists(lists))