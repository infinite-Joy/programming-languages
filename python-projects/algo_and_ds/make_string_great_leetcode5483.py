"""
https://leetcode.com/contest/weekly-contest-201/problems/make-the-string-great/
we will probably need one single iteration on the string.
and then we will mutate the string as we go.
since the string is immutable this have space complexity of O(n)
for time complexity this will be O(n)
so we will need kind of an i to keep track if we have reached the end.
=================================
"""


class Solution:
    def make_good_rec(self, string: str, idx: int) -> str:
        print(string, idx)
        if idx >= len(string):
            return string
        if (idx > 0 and string[idx-1].lower() == string[idx].lower() and (
            (string[idx-1].islower() and string[idx].isupper()) or
            (string[idx-1].isupper() and string[idx].islower()))):
            return self.make_good_rec(string[:idx-1]+string[idx+1:], idx-1)
        return self.make_good_rec(string, idx+1)

    def makeGood(self, s: str) -> str:
        return self.make_good_rec(s, 1)


s = Solution()

print(s.makeGood("abBAcC"))
print(s.makeGood("Pp"))
