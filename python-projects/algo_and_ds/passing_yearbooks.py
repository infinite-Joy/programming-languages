"""
passing yearbook

https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=146466059993201&c=1062635970997589&ppid=454615229006519&practice_plan=0

this is basically a graph problem.

for each cycle the number of people that are part of the cycle will hvae that many signatures.

so basically to build the mapping for the different cycles.

since all the elements in the array are gone through once this is a graph problem

"""

from collections import deque, Counter


def bfs(arr):
    found_cycle = 1
    cycle_mapping = [-1] * len(arr)
    queue = deque([arr[0]]) # 3
    visited = [False] * len(arr)
    visited[0] = True
    not_done = set(arr) # do not include the first elem. that is already being considered # 241
    # cycle_mapping[0] = found_cycle

    while queue or not_done:
        print('queue', queue, cycle_mapping)
        elem = queue.popleft() or not_done.pop() # 3
        visited[elem-1] = True
        # not_done.remove(elem)
        # cycle_mapping[0] = found_cycle
        nelem = arr[elem-1] # 1
        print('nelem', nelem)
        if visited[nelem-1]:
            print('visited')
            # cycle is done
            if not_done:
                val = not_done.pop()
                queue.append(val)
                found_cycle += 1 # update the cycle identifier
                cycle_mapping[val - 1] = found_cycle
        else:
            queue.append(nelem) # queu=1
            not_done.remove(nelem) # 24
            cycle_mapping[nelem-1] = found_cycle

    cycle_counts = Counter(cycle_mapping)
    cycle_mapping = [cycle_counts[x] for x in cycle_mapping]
    return cycle_mapping


arr = [3, 2, 4, 1]
print(arr)
print(bfs(arr))