"""

interval list intersections leetcode 986

Input: A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]


[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

[1,5], [0,2]

this is a 2 pointer solution

(1,2) (5,5) (8, 10) (15, 23) ()

while disjoint add it to the solution

compare: i, j

    i = 0
    j = 0
    start = compare i j
    while i within arr1 and j within arr2:
        compare start i
        compare start j

so we will  be using stacks for this

the time complexity of this is O(size of arr a + size of arr b)
space complexity: O(size of arr a + size of arr b)


"""

from collections import dequeu
class Solution:
    def compare(self, sol, queue, arr, i): # [8,12]
        while queue and queue[0][1] < arr[i][0]:
            queue.popleft() # [5, 10]
        if queue:
            last = queue[0]
            sol.append([arr[i][0], last[1]])
        queue.append(arr[i]) # [5, 10]
        return i + 1
    def move_through(self, sol, arr1, arr2):
        i = 0
        j = 0
        queue = deque([])
        while i < len(arr1) and j < len(arr2):
            if arr[i] <= arr2[j]: # [5,10], [8,12]
                i = self.compare(sol, queue, arr1, i) # i would become 1
            else:
                j = self.compare(sol, queue, arr2, j) # j = 1
        if i < len(arr1):
            i = self.compare(sol, queue, arr1, i)
        if j < len(arr2):
            j = self.compare(sol, queue, arr2, j)
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        sol = []
        arr1 = A
        arr2 = B
        self.move_through(sol, arr1, arr2)
        return sol


# test case
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
