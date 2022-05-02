"""
this looks like an implementation of sliding window.

this is a DP solution

let me try the recursion first

time and space is O(n2)
and space complexity O(n2)

"""


def is_valid(s, i, j):
    # print(s, i, j, 12)
    stack = []
    if i >= j:
        return True
    for ch in range(i, j+1):
        ch = s[ch]
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if stack:
                stack.pop()
            else:
                return False
    #     print(stack)
    # print(stack)
    if len(stack) == 0:
        return True
    return False

def dfs(s, i, j):
    if i == j:
        # print(s, i, j, 0)
        return 0
    if is_valid(s, i, j):
        # print(s, i, j, j - i + 1, 32)
        return j - i + 1
    else:
        # print(s, i, j, max(dfs(s, i+1, j), dfs(s, i, j-1), dfs(s, i+1, j-1)), 35)
        return max(dfs(s, i+1, j), dfs(s, i, j-1), dfs(s, i+1, j-1))
    
s = '(()'
print(dfs(s, 0, len(s)-1))


def longest_valid_parenthesis(s):
    stack = [-1]
    maxlen = 0
    if s == '':
        return 0
    for i, ch in enumerate(s):
        # print(stack)
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                maxlen = max(maxlen, i - stack[-1] + 1)
    return maxlen

s = '(()'
print(longest_valid_parenthesis(s))