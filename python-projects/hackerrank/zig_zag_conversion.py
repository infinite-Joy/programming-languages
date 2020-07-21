"""
https://leetcode.com/problems/zigzag-conversion/
we should probably have n lists.
where if
PI    N
A   L S  I G
Y A   H R
P     I

complexity: O(n)
space: O(1)

"""


def zig_zag(s, n):
    sols = [[] for _ in range(n)]
    for i in range(n):
        j = 0
        while j <= len(s)//n:
            if i == 0:
                item = (n-1)*2*j
                if item >= 0 and item < len(s):
                    sols[i].append(s[item])
            elif i == n-1:
                #__import__('pdb').set_trace()
                item = (n-1)*(2*j+1)
                if item > 0 and item < len(s):
                    sols[i].append(s[item])
            else:
                #__import__('pdb').set_trace()
                item1 = (n-1)*2*j - i
                if item1 > 0 and item1 < len(s):
                    sols[i].append(s[item1])
                item2 = (n-1)*2*j + i
                if item2 > 0 and item2 < len(s):
                    sols[i].append(s[item2])
            j += 1
    print(sols)
    for i in range(len(sols)):
        sols[i] = "".join(sols[i])
    print("".join(sols))
    return sols

print(zig_zag("PAYPALISHIRING", 3))
#assert zig_zag("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR'
