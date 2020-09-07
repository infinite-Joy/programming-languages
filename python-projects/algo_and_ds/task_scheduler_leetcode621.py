"""

# TODO this is not working

task scheduler

leetcode 621

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

we can try this using a max heap

[(3, 0, a), (3, 0, b)]
a=0, b=0

i = 0 so a and [(2, 2, a), (3, 0, b)] and a=3
i=1 and nothing in b so b and [(2, a), (2, b)] and a=3, b=4
i = 2 and less than a so idle and [(2, a), (2, b)] and a=3, b=4
i = 3 and = a so a and [(1, a), (2, b)] and a=6, b=4
i = 4 and = b so b and [(1, a), (1, b)] and a = 6, b=7
null and

time complexity

so basically i can keep a max heap of the elements and a counter to see any of the items are still hot

time complexity: O(number of distinct items)
space complexity: O(number of distinct items)

"""

from heapq import heappop, heappush, heapreplace, heapify
from collections import Counter
from collections import defaultdict
from typing import List

class Solution:
    def preprocess(self, tasks):
        counts = Counter(tasks)
        heap = [(-c, t) for t, c in counts.items()]
        heapify(heap)
        return heap

    def units_count(self, heap, n):
        availability = defaultdict(int)
        counter = 0
        #__import__('pdb').set_trace()
        while heap:
            rem, next_task = heap[0]
            if availability[next_task] <= counter:
                heappop(heap)
                if rem < -1:
                    heappush(heap, (rem + 1, next_task))
                    counter += 1
                availability[next_task] = counter + n
            print(heap, availability)
        return counter

    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = self.preprocess(tasks)
        print(heap)
        return self.units_count(heap, n)

# test cases

tasks = ["A","A","A","B","B","B"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks, n))

tasks = ["A","A","A","B","B","B"]
n = 0
sol = Solution()
print(sol.leastInterval(tasks, n))

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks, n))
