"""
permutation in string

https://leetcode.com/problems/permutation-in-string/

we can just create a hash and if the hashes are the same we can check the strings are the same as well

if they are the same we can check the actual string

or we can use a counter for that

similar to the lowest substring and use a two pointer for that, similar to that

worst time complexity is O(n*m)

"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        if not s1:
            return False
        if s1 and not s2:
            return False

        string1 = Counter(s1)
        curr_string = {}
        i = 0
        chars = 0
        for j, ch in enumerate(s2):
            print(curr_string)
            #__import__('pdb').set_trace()
            if ch in string1:
                if ch not in curr_string:
                    curr_string[ch] = 0
                curr_string[ch] += 1
                chars += 1
                if chars == len(s1):
                    if string1 == curr_string:
                        return True
            else:
                i = j
                curr_string = {}
                chars = 0

            while ch in string1 and ch == s2[i] and curr_string[ch] > string1[ch]:
                i += 1
                curr_string[ch] -= 1
                chars -= 1
        return False


# test cases
s1 = "ab"
s2 = "eidbaooo"
sol = Solution()
print(sol.checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaooo"
sol = Solution()
print(sol.checkInclusion(s1, s2))

s1 = "adc"
s2 = "dcda"
sol = Solution()
print(sol.checkInclusion(s1, s2))
