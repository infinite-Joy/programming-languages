"""
rotate the lock
this is a graph problem
next start of 0000 -> 1000 or 9000 and we need to do bfs
time complexity: 4*10
space complexity: edit distance between the starting amd tje emd

from collections import deque
class Solution:
    def __init__(self):
        self.nums = [str(i) for i in range(10)]
    def same(self, config, other):
        for el1, el2 in zip(one, other):
            if el1 == el2:
                return True
    def next_state(self, state, deadends):
        for pos in range(4):
            val = int(state[pos])
            newstates = state[:pos] + self.nums[pos - 1] + state[pos + 1:], state[:pos] + self.nums[(pos + 1) % 10] + state[pos + 1:]
            for ns in newstates:
                if ns not in deadends:
                    yield ns
    def bfs(self, start, end, deadends):
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            state, moves = queue.popleft()
            if state == end:
                return moves
            for next_state in self.next_state(state, deadends):
                if next_state not in visited:
                    queue.append((next_state, moves + 1))
                    visited.add(next_state)
        return -1
def openLock(self, deadends: List[str], target: str) -> int:
    deadends = set(deadends)
    target_num = sum(int(x) for x in target)
    target_string = list(target)


"""

from collections import deque
from typing import List
class Solution:
    def __init__(self):
        self.nums = [str(i) for i in range(10)]
    def next_state(self, state, deadends):
        for pos in range(4):
            val = int(state[pos])
            newstates = state[:pos] + self.nums[val - 1] + state[pos + 1:], state[:pos] + self.nums[(val + 1) % 10] + state[pos + 1:]
            for ns in newstates:
                if ns not in deadends:
                    yield ns
    def bfs(self, start, end, deadends):
        queue = deque([(start, 0, [start])])
        visited = {start}
        while queue:
            state, moves, path = queue.popleft()
            print(state, moves, path)
            if state == end:
                return moves
            for next_state in self.next_state(state, deadends):
                if next_state not in visited:
                    newpath = path[::] + [next_state]
                    queue.append((next_state, moves + 1, newpath))
                    visited.add(next_state)
        return -1
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        return self.bfs("0000", target, deadends)


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
sol = Solution()
print(sol.openLock(deadends, target))
