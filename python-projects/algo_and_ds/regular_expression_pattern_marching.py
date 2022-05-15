"""
https://www.youtube.com/watch?v=HAA8mgxlov8&t=1024s

https://leetcode.com/problems/regular-expression-matching/

brute force


pattern: break based on *
for each pattern get the largest string that matches this.
have i and j. if match found then go on to the next pattern.
if all the strings are complete then this is return True



"""


def get_star(pattern):
    subpatterns = []
    i = 0
    for j, ch in enumerate(pattern):
        if ch == "*":
            subpatterns.append(pattern[i:j+1])
            i = j+1
    subpatterns.append(pattern[i:j+1])
    return subpatterns

def validate_with_star(string, subpattern, i):
    """
    cases:
        the characters do not match
    
    
    """
    j = i
    ch_before_star = None
    for j in range(i, len(string)):
        if ch_before_star is not None:
            if string[j] != subpattern[j]:
                return False
            elif subpattern[j] == '.':
                pass # go to the next loop
            elif subpattern[j] == '*':
                # get the previous character
                ch_before_star = subpattern[j-1]
                if ch_before_star == '.':
                    pass
                else
        # else:




def validate_without_star(string, pattern):
    if len(string) != len(pattern):
        return False
    for s, p in zip(string, pattern):
        if p != '.' and s != p:
            return False
    return True

def is_match(s, p):
    subpatterns = get_star(p)
    print(subpatterns)
    i = 0
    j = 0
    for subpattern in subpatterns:
        if subpattern[-1] != "*":
            j = i + len(subpattern)
            substring = s[i:j]
            if validate_without_star(substring, subpattern):
                i = j
            else:
                return False
        else:
            # TODO implement this
            while i < len(s) and j < len(s):
    # if all subpatterns are done and we still have strings left then this is a false
    return s[i:] == ''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return is_match(s, p)
        

print(is_match('ab', 'a'))
print(is_match('ab', 'a.'))
print(is_match('ab', 'ab'))
print(is_match('ab', 'ac'))


# the above solution did not work. this is actually a DP problem

# inspiration: https://www.youtube.com/watch?v=HAA8mgxlov8


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j, s, memo=None):
            memo = {} if memo is None else memo
            
            # memo case
            if (i, j) in memo:
                return memo[(i, j)]
            
            # base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            # normal case
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j+1) < len(p) and p[j+1] == '*':
                memo[(i, j)] = (dfs(i, j+2, s, memo) or         # do not take the *
                                match and dfs(i+1, j, s, memo)) # using the *
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i+1, j+1, s, memo)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0, s)