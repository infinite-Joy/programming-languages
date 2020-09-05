"""

find all anagrams in a string

438. Find All Anagrams in a String

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

we can do a rolling hash kind of a scenario

if ther rolling hash is fine then we can check if the strings are fine

for anagrams it is just the addition of the numbers since this is an anagram

"""
from string import ascii_letters
from typing import List
class Solution:
    def check_eq(self, p, s, start, end):
        __import__('pdb').set_trace()
        if p == s[start:end+1]:
            return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        shash = 0
        phash = 0
        length = len(p)
        solution = []
        for item in p:
            phash += ord(item)
        print(phash)
        for front in range(len(s)):
            shash += ord(s[front])
            start = front - length
            if front >= length - 1:
                __import__('pdb').set_trace()
                if start >= 0:
                    shash -= ord(s[start])
                print(shash)
                if shash == phash and self.check_eq(p, s, start, front):
                    solution.append(start)
        return solution

# test cases
s = "cbaebabacd"
p = "abc"
sol = Solution()
print(sol.findAnagrams(s, p))
