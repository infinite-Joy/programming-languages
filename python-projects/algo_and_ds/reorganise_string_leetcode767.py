"""

reorganising string

this feels like can be done in O(N)

Input: S = "aab"
Output: "aba"

take the count of the letters

take the maximum. then create a list of lists

for each value in the others put it in the list.

and then once done return it. if the other values are done then return empty string

should take O(size of the string)

we can do it similar to the cooldown period with cooldown == 1

"""

# solution based on heaps

from collections import Counter
from heapq inport heapify, heappop, heappush
class Solution:
    def preprocess(self, S):
        counts = Counter(S)
        heap = [[-i, s] for s, i in counts.items()]
        heapify(heap)
        return heap
    def reorganise(self, string):
        heap = self.preprocess(string)
        sol = []

        # take the first element and then keep it
        prev = heappop(heap)
        sol.append(prev[1])

        while heap:
            curr = heappop(heap)
            if curr:
                sol.append(curr[1])
            else:
                if prev[0] > 1:
                    return ""
            prev[0] += 1
            if prev[0] < 0:
                heappush(heap, prev)
            prev = curr
        sol.append(prev[1])

        return sol

    def reorganizeString(self, S: str) -> str:
        sol = self.reorganise(S)
        return "".join(sol)

# the putting things into the middle

from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def reorganise(self, string):
        counts = Counter(string)
        maxval, maxstring = 0, ""
        for s, val in counts.items():
            maxval = max(maxval, val)
            if maxval == val:
                maxstring = s

        final_out = [None for _ in range(2 * maxval)]
        for i in range(maxval):
            final_out[2 * i] = maxstring
        i = 1
        for s, count in counts.items():
            for c in range(count):
                final_out[i] = s
                i += 2
        return final_out

    def reorganizeString(self, S: str) -> str:
        final_out = self.reorganise(S)
        if all(string):
            return "".join(final_out)
        return ""

# test cases
S = "aab"
sol = Solution()
print(sol.reorganizeString(S))
