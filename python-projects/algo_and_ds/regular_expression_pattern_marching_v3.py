"""
this is a dp problem



"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(s, p):
            if len(s) == 1 and len(p) == 1 and s == p:
                return True
            elif len(s) == 1 and len(p) == 1 and p == '.':
                return True
            elif len(s) == 1 and len(p) == 0:
                return False
            elif len(s) == 0 and len(p) == 0:
                return True
            else:
                if s[0] != p[0] and p[0] != '.':
                    return False
                elif s[0] != p[0] and p[1] != '*':
                    return False
                elif s[0] != p[0] and p[0] == '.':
                    return dp(s[1:], p[1:])
                elif s[0] != p[0] and p[1] == '*':
                    return dp(s, p[2:])
                elif s[0] == p[0]:
                    if p[1] == "*":
                        return dp(s, p[2:]) or dp(s[1:], p[2:])
                    else:
                        return dp(s[1:], p[1:])
                elif p[0] == '.' and p[1] == '*':
                    return dp(s[1:], p) or dp(s, p[2:])
                
            return dp(s, p)

def dp(s, p):
    # print(s, p)
    if len(s) == 1 and len(p) == 1 and s == p:
        return True
    elif len(s) == 1 and len(p) == 1 and p == '.':
        return True
    elif len(s) > 0 and len(p) == 0:
        return False
    elif len(s) == 0 and len(p) > 0:
        if len(p) == 2 and p[1] == '*':
            return True
        else:
            return False
    elif len(s) == 0 and len(p) == 0:
        return True
    else:
        if p[0] == '.' and p[1] == '*':
            return dp(s[1:], p) or dp(s, p[2:])
        elif s[0] != p[0] and p[0] != '.':
            return False
        elif s[0] != p[0] and p[1] != '*':
            return False
        elif s[0] != p[0] and p[0] == '.':
            return dp(s[1:], p[1:])
        elif s[0] != p[0] and p[1] == '*':
            return dp(s, p[2:])
        elif s[0] == p[0]:
            if p[1] == "*":
                return dp(s[1:], p) or dp(s[1:], p[2:])
            else:
                return dp(s[1:], p[1:])
        

# s = 'aa'
# p = 'a*'
# print(dp(s, p))

s = 'aa'
p = '.*'
print(dp(s, p))