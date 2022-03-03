# jump game III
"""
https://leetcode.com/problems/jump-game-iii/

looks like this is a graph problem with BFS

think about the problem and give the solution
look into the edge cases as well
"""

from collections import deque

def get_edges(arr, curr):
    if curr + arr[curr] < len(arr):
        yield curr + arr[curr]
    if 0 <= curr - arr[curr]:
        yield curr - arr[curr]


def bfs(arr, start):
    visited = [False for _ in arr]
    processed = [False for _ in arr]
    queue = deque([start])
    visited[start] = True

    while queue:
        curr = queue.popleft()
        elem = arr[curr]
        print('curr elem', curr, elem)
        # process the edge. business logic
        if elem == 0:
            return True
        processed[curr] = True

        for edge in get_edges(arr, curr):
            if visited[edge] is False:
                queue.append(edge)
                visited[edge] = True

    return False

arr = [4,2,3,0,3,1,2]
start = 5
print(start, arr)
print(bfs(arr, start))
print('-' * 100)

arr = [4,2,3,0,3,1,2]
start = 0
print(start, arr)
print(bfs(arr, start))
print('-' * 100)

arr = [0, 1]
start = 1
print(start, arr)
print(bfs(arr, start))
print('-' * 100)