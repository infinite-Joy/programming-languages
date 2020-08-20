# solution using backtracking
# time complexity O( fact n )


values = {'(': 1, ')': -1}

def process_sol(sol_arr):
    global SOL
    SOL.append("".join(sol_arr))

def is_valid(n, arr, val):
    if len(arr) == 2*n and val == 0:
        return True

def construct_candidates():
    yield from values.keys()

def makemove(arr, bracket, val):
    arr.append(bracket)
    return val + values[bracket]

def unmakemove(arr, val):
    bracket = arr.pop()
    return val - values[bracket]

from math import fabs
def ok(partial_sol, n, partialval):
    return len(partial_sol) <= 2*n and partialval >= 0 and n >= fabs(partialval)

def backtrack(n, partial_sol, val):
    print(n, partial_sol, val)
    if is_valid(n, partial_sol, val):
        process_sol(partial_sol)
    else:
        for candidate in construct_candidates():
            val = makemove(partial_sol, candidate, val)
            if ok(partial_sol, n, val):
                print('inside ok', partial_sol)
                backtrack(n, partial_sol, val)
            val = unmakemove(partial_sol, val)

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        global SOL
        SOL = []
        partial_sol = []
        backtrack(n, partial_sol, 0)
        print(SOL)


s = Solution()
s.generateParenthesis(3)

