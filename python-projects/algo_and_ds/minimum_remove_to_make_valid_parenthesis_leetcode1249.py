"""

minimum remove to make valid parenthesis

leetcode 1249

balance = 0
iterate on the string
    ( => balance++
    ) => balance -- if balance > 0
        else:
            make the string None

iterate on the string from the end

    ) => balance ++
    ( => balance-- if balance
        else
            make the string None

join the final string

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

time complexity: O(n)
space complexity: O(n)


"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        final = list(s)
        balance = 0
        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            elif ch == ')':
                if balance > 0:
                    balance -= 1
                else:
                    final[i] = None
            else:
                pass

        balance = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == ')':
                balance += 1
            elif ch == '(':
                if balance > 0:
                    balance -= 1
                else:
                    final[i] = None
            else:
                pass

        return "".join(i for i in final if i)
