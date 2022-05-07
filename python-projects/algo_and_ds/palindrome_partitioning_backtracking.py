"""
paritioning. probably trying to do this using backtracking




"""


def ispalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def backtrack(s, i):
    parts = []
    for j in range(i, len(s)):
        if ispalindrome(s, i, j):
            print('ispalindrome', i, j)
            other_parts = backtrack(s, j+1)
            print(f'before adding current {other_parts=}, {[s[i:j+1]]=}', i, j+1)
            if other_parts:
                other_parts = [[s[i:j+1]] + x for x in other_parts]
            else:
                other_parts = [[s[i:j+1]]]
            print(f'{other_parts=}', i, j+1)
            parts = parts + other_parts
    return parts

print(ispalindrome('a', 0, 0))
print(ispalindrome('aa', 0, 1))
print(ispalindrome('aab', 0, 2))
print('#'*10)

print(backtrack('aab', 0))


# accepted solition
"""
paritioning. probably trying to do this using backtracking




"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def ispalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(s, i):
            parts = []
            for j in range(i, len(s)):
                if ispalindrome(s, i, j):
                    # print('ispalindrome', i, j)
                    other_parts = backtrack(s, j+1)
                    # print(f'before adding current {other_parts=}, {[s[i:j+1]]=}', i, j+1)
                    if other_parts:
                        other_parts = [[s[i:j+1]] + x for x in other_parts]
                    else:
                        other_parts = [[s[i:j+1]]]
                    # print(f'{other_parts=}', i, j+1)
                    parts = parts + other_parts
            return parts
                    
        return backtrack(s, 0)