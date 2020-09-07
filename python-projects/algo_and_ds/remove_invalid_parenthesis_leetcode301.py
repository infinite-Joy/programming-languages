"""

remove invalid parenthesis

leetcode 301

first solution that comes to mind is the backtracking solution

solution is probably length * 2 ** length

thinking of a single pass solution

maybe we can put things into the stack

use both queue and stack

"   (   )   (   )   )   (   )"

queue
(  []  (
)  [()]
(   [()]    (
)   [()()]
)   [()()]  )
(   [()()]  )(
)   [()()()] )

stack

"(a)())()"
queue
(   [(]  (
a   [(a]    (
)   [(a)]
(   [(a)(]  (
)   [(a)()]
)   [(a)()]
(   [(a)()] (
)   [(a)()()]

this is not working out.

something like from front to back and a 2 pass solution

finally according to the answer they are giving that tthis is a backtrcking solution

def valid

def backtrack(curr, s, i):





"""

from heapq import heappush

class Solution:
    def __init__(self):
        self.sols = []
    def valid(self, curr):
        balance = 0
        for ch in curr:
            if ch == '(':
                balance += 1
            elif ch == ')':
                balance -= 1
            else:
                pass
        return balance == 0
    def process_sol(self, curr, s):
        heappush(self.sols, (len(s) - len(curr)), "".join(curr))

    def backtrack(self, curr, s, i):
        if self.valid(curr):
            self.process_sol(curr, s)
        else:
            ch = s[i]
            curr.append(ch)
            backtrack(curr, s, i+1)
            curr.pop()
            backtrack(curr, s, i+1)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.backtrack([], s, 0)
        minval, _ = self.sols[0]
        sol = []
        while self.sols and self.sols[0][0] == minval:
            sol.append(heappop(self.sols)[1])
        return sol
