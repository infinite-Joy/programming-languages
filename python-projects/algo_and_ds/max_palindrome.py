"""
https://leetcode.com/problems/longest-palindromic-substring/

should be using dynamic programming and recursion
babad

should have a map of the duplicated elements
so we can consider a palindrome to be something like
mapping
cbabc => left == right => mapping[left] = right
moving on to b
c != a hence no change
move on to a

complexity of this is On2
================
"""
# https://leetcode.com/problems/longest-palindromic-substring/

from functools import lru_cache

class Solution(object):
    @lru_cache()
    def is_palindrome(self, a):
        """check for palindromicity

        Args:
            a (str): the input string

        Returns:
            bool
        """
        if len(a) == 1 or len(a) == 0:
            return True
        if a[0] == a[-1]:
            return self.is_palindrome(a[1:-1])

    def longestPalindrome(self, a):
        """find the largest palindrome size

        Args:
            a (str): the input string

        Returns:
            int: the maximum size
        """
        if len(a) == 0:
            return ""
        max_palindrome_size = 0
        sol = None
        for i in range(len(a)):
            #__import__('pdb').set_trace()
            span = 0
            # even case
            if i+1<len(a) and a[i] == a[i+1]:
                while i >= span and i + span + 2 <= len(a):
                    word = a[i-span:i+span+2]
                    if self.is_palindrome(a[i-span:i+span+2]) is True:
                        max_palindrome_size = max(max_palindrome_size, len(word))
                        if max_palindrome_size == len(word):
                            sol = word
                    span += 1
            else:
                # odd case
                while i >= span and i + span + 1 <= len(a):
                    word = a[i-span:i+span+1]
                    #print(word)
                    if self.is_palindrome(word) is True:
                        max_palindrome_size = max(max_palindrome_size, len(word))
                        if max_palindrome_size == len(word):
                            sol = word
                    span += 1
        return sol

print(Solution().longestPalindrome("babad"))
print("%"*10)
print(Solution().longestPalindrome("cbbd"))
