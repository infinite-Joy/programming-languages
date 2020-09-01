"""

word break problem seems like a famous problem

the established method is using the dynamic programming

word break problem is solved using dp

the recurrence is dp[i] = dp[j] & dp[i:j] for all j in 0 to i-1

for more explanation see this https://www.youtube.com/watch?v=1U4jQusbeJc

time complexity : O(n2)
space complexity: O(n)

"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string = s
        wordDict = set(wordDict)
        dp = [False for _ in range(len(string) + 1)]
        dp[0] = True # this is the base case or the empty case. we dont select any word from the dictionary for the empty string

        for i in range(1, len(string)+1):
            for j in range(i-1, -1, -1):
                if dp[i] is False and dp[j] and string[j:i] in wordDict:
                    dp[i] = True
            print(dp)

        return dp[len(string)]

string = "leetcode"
wordDict = ["leet", "code"]
s = Solution()
print(s.wordBreak(string, wordDict))

string = "applepenapple"
wordDict = ["apple", "pen"]
s = Solution()
print(s.wordBreak(string, wordDict))

string = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = Solution()
print(s.wordBreak(string, wordDict))
