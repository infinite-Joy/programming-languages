"""

we can use a max heap to understand what is the smallest number that can be found
this is a greedy sum as smallest from the two would be the values.
once i and j reach the last values then we know that the sums have been reached.
so this is a two pointer solution as well

THis works well since the insertion is O(log)

this is an O(n2 solution)

interesting solution is here
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation

this will be done in O(n)

tjis 


"""

from heapq import heappush, heappop, nlargest, heapreplace

def get_smallest_pairs(nums1, nums2, k):
    i = 0
    iend = k
    heap = [(0, 0, 0)]
    for j in range(k):
        i = 0
        while i < iend:
            if len(heap) <= k:
                heappush(heap, (-(nums1[i] + nums2[j]), i, j))
            elif nums1[i] + nums2[j] > abs(heap[0][0]):
                iend = i
            else:
                heapreplace(heap, (-(nums1[i] + nums2[j]), i, j))
            i += 1
        print(i, j, heap)

    vals = [heappop(heap) for _ in range(len(heap))][::-1]
    vals = vals[1:]
    return [(nums1[x], nums2[y]) for _, x, y in vals]


nums1 = [1,7,11, 16]
nums2 = [2,9,10,15]
k = 4
print(get_smallest_pairs(nums1, nums2, k))

# this does not work. has some issues.


# This is mostly working and not working

from heapq import heappush, heappop, nlargest, heapreplace


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def get_smallest_pairs(nums1, nums2, k):
            swap = False
            if len(nums1) > len(nums2):
                swap = True
                nums1, nums2 = nums2, nums1
            i = 0
            iend = min(k, len(nums1))
            heap = [(0, 0, 0)]
            for j in range(min(k, len(nums2))):
                i = 0
                while i < iend:
                    if len(heap) <= k:
                        heappush(heap, (-(nums1[i] + nums2[j]), i, j))
                    elif nums1[i] + nums2[j] > abs(heap[0][0]):
                        iend = i
                    else:
                        heapreplace(heap, (-(nums1[i] + nums2[j]), i, j))
                    i += 1
                # print(i, j, heap)

            vals = [heappop(heap) for _ in range(len(heap))][::-1]
            vals = vals[1:]
            if swap:
                return [(nums2[y], nums1[x]) for _, x, y in vals]
            return [(nums1[x], nums2[y]) for _, x, y in vals]
        
        return get_smallest_pairs(nums1, nums2, k)