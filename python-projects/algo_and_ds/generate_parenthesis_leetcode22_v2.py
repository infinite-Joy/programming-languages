"""
question: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

there are only two combinations that can be done at any single point in time.

complexity is 2*n
"""

def get_valid_option(stack, done=False):
    if stack == 0:
        if done is False:
            return ['(']
        else:
            return []
    elif stack > 0:
        if done is True:
            return [')']
        else:
            return ['(', ')']


def incr_stack(stack, option):
    if option == '(':
        return stack + 1
    else:
        return stack - 1

def incr_done(done, option):
    if option == ')':
        return done + 1
    else:
        return done


def generate_parenthesis(ans, n, done=0, buildup='', stack=0):
    print(f'{ans=}, {n=}, {done=}, {buildup=}, {stack=}')
    if done>=n:
        ans.append(buildup)
        return
    for option in get_valid_option(stack, done=(stack + done)>=n):
        # [], 1, 0, (, 1
        # [], 1, 1, (), 1
        generate_parenthesis(ans, n, done=incr_done(done, option), buildup=buildup + option, stack=incr_stack(stack, option))



ans = []
n = 1
generate_parenthesis(ans, n, done=0, buildup='', stack=0)
print(ans)
print('#' * 30)

######################################

ans = []
n = 2
generate_parenthesis(ans, n, done=0, buildup='', stack=0)
print(ans)
print('#' * 30)

######################################

ans = []
n = 3
generate_parenthesis(ans, n, done=0, buildup='', stack=0)
print(ans)
print('#' * 30)