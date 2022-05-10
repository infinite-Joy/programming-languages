"""

get count of elements 
get the next elem based on the 
also we can have a queue of n
we can also have a queue. whenever we get the elem. we decrement the count and add it back to the heap

this is a greedy solution

"""

from collections import Counter, deque
from heapq import heappush, heappop, heapify


def task_scheduler(tasks, n):
    counts = Counter(tasks)
    heap = [[-c, t] for t, c in counts.items()] # since heap in python is min heap
    heapify(heap)
    queue = deque([])
    elem_in_queue = set()
    count = 0
    print(f'{heap=}')
    # fill the queue with the possible first elements
    while len(queue) < n+1:
        if heap:
            nextelem = heappop(heap)
            queue.append(nextelem)
            elem_in_queue.add(nextelem[1])
        else:
            queue.append(None)
    print(f'{heap=}, {queue=}')

    while heap or elem_in_queue:
        outgoing = queue.popleft()
        count += 1
        if outgoing is not None:
            elem_in_queue.remove(outgoing[1])
            outgoing[0] += 1
            if outgoing[0] < 0:
                heappush(heap, outgoing)
                
        if heap:
            nextelem = heappop(heap)
            queue.append(nextelem)
            elem_in_queue.add(nextelem[1])
        else:
            queue.append(None)
        print(f'{heap=}, {queue=}')

    return count

tasks = ["A","A","A","B","B","B"]
n = 2
print(task_scheduler(tasks, n))


tasks = ["A","A","A","B","B","B"]
n = 0
print(task_scheduler(tasks, n))

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(task_scheduler(tasks, n))

# ===========================
# this works mostly. but probably can be made better

"""

get count of elements 
get the next elem based on the 
also we can have a queue of n
we can also have a queue. whenever we get the elem. we decrement the count and add it back to the heap

"""

from collections import Counter, deque
from heapq import heappush, heappop, heapify


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def task_scheduler(tasks, n):
            counts = Counter(tasks)
            heap = [[-c, t] for t, c in counts.items()] # since heap in python is min heap
            heapify(heap)
            queue = deque([])
            elem_in_queue = set()
            count = 0
            # print(f'{heap=}')
            # fill the queue with the possible first elements
            while len(queue) < n+1:
                if heap:
                    nextelem = heappop(heap)
                    queue.append(nextelem)
                    elem_in_queue.add(nextelem[1])
                else:
                    queue.append(None)
            # print(f'{heap=}, {queue=}')

            while heap or elem_in_queue:
                outgoing = queue.popleft()
                count += 1
                if outgoing is not None:
                    elem_in_queue.remove(outgoing[1])
                    outgoing[0] += 1
                    if outgoing[0] < 0:
                        heappush(heap, outgoing)

                if heap:
                    nextelem = heappop(heap)
                    queue.append(nextelem)
                    elem_in_queue.add(nextelem[1])
                else:
                    queue.append(None)
                # print(f'{heap=}, {queue=}')

            return count
        
        return task_scheduler(tasks, n)