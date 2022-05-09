"""
Here we can use quick select to get the values.

time complexity: O(nlogk)
"""

import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def partition(distances, l, r):
            p = r
            firsthigh = 0
            for el in range(l, r+1):
                if distances[el][0] <= distances[p][0]:
                    distances[firsthigh], distances[el] = distances[el], distances[firsthigh]
                    firsthigh += 1
            distances[p], distances[firsthigh] = distances[firsthigh], distances[p]
            return p
            
        def find_k_closest(distances, l, r, k):
            if l == r:
                return l
            p = partition(distances, l, r)
            if p == k - 1:
                return distances[p][1]
            elif p < k:
                return find_k_closest(distances, l, p-1, k)
            else:
                return find_k_closest(distances, p+1, r, k)
            
        def calculate_distances(points):
            distances = []
            for i, (p, q) in enumerate(points):
                distance = math.sqrt(p**2 + q**2)
                distances.append((distance, i))
            return distances
        
        def main(points, k):
            distances = calculate_distances(points) # [(distance, index)]
            pos = find_k_closest(distances, 0, len(distances)-1, k) # this will do the partition 
            return points

"""
but this was not what was asked in the question.
to get that we have to use the heap method
"""

from heapq import heappush, heapreplace

def calculate_distances(points):
    distances = []
    for i, (p, q) in enumerate(points):
        distance = math.sqrt(p**2 + q**2)
        distances.append((-distance, i))
    return distances

def main(points, k):
    distances = calculate_distances(points) # [(distance, index)]
    print(distances)
    heap = []
    print('starting the heap')
    for d in distances:
        if len(heap) == 0 or len(heap) < k:
            heappush(heap, d)
        else:
            if d[0] > heap[0][0]:
                heapreplace(heap, d)
        print(heap)
    return [points[x[1]] for x in heap] # get the points
    
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(points)
print(main(points, k))

#############################

# final solution

"""
Here we can use quick select to get the values.

time complexity: O(nlogk)
space: O(n)
"""

import math
from heapq import heappush, heapreplace

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate_distances(points):
            distances = []
            for i, (p, q) in enumerate(points):
                distance = math.sqrt(p**2 + q**2)
                distances.append((-distance, i))
            return distances
        
        def main(points, k):
            distances = calculate_distances(points) # [(distance, index)]
            # print(distances)
            heap = []
            for d in distances:
                if len(heap) == 0 or len(heap) < k:
                    heappush(heap, d)
                else:
                    if d[0] > heap[0][0]: # greater becase we are working in the negative space here
                        heapreplace(heap, d)
            return [points[x[1]] for x in heap] # get the points
            
        return main(points, k)