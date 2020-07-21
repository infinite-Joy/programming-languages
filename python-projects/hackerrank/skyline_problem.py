"""
218. The Skyline Problem

references: https://briangordon.github.io/2014/08/the-skyline-problem.html

Great solution. I adapted the explanation here https://briangordon.github.io/2014/08/the-skyline-problem.html for this specific implementation.

1.First, sort the critical points by its left endpoints. We treat R in (R,0,None) as left endpoint. Then scan across the critical points from left to right.

2.We only push right end points onto the heap. Think of it as a proxy for the entire rectangle. The key is its negative height because heapq implements min-heap. The heap keeps track of the current max height.

3.In the for-loop, when we encounter a left end point that is larger than maxheight (hp[0][0]), we pop hp until all right endpoints smaller than the current left end point are gone. Interestingly, we don't traverse through the heap and remove a rectangle every time an incoming left endpoint comes along. Because we only care about the max height, aka, heap[0][0].

3.Finally, after updating the heap, we check whether the current max height (hp[0[0]) differs from the last max height (res[-1][1] ), if so, we append the hp[0][0] as the height .
In short,
a. if the height at current left point is the first in the heap (after we just updated it),then negH == -hp[0][0].
b. if the height at current left point is not the first in the heap ,that means it is either completely overshadowed by the taller buildings or it will be used when the taller building is popped from the heap. In the second case, don't forget that our lower building's right endpoint is still in the heap, when taller building is popped from the heap, and the lower building's height becomes the max height.

O(nlogn) time. O(n) space

"""

from heapq import heappop, heappush
import math

class Solution:
    def get_skyline(self, buildings):
        # add start building events
        # also add end building events (act as buildings  with 0 height)
        # and sort the events in left to right order
        events = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings]
        events.sort()
        print(events)

        res = [[0,0]]
        live = [(0, math.inf)]
        for pos, negH, R in events:
            print((pos, negH, R), live, res)
            print()
            print()
            #__import__('pdb').set_trace()
            # pop the buildings that are already ended
            while live[0][-1] <= pos:
                heappop(live)
            # if its the start building make the building alive
            if negH:
                heappush(live, (negH, R))
            # if previous keypoint height != current highest height, edit the
            # result
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]



buildings = [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]
Solution().get_skyline(buildings)
