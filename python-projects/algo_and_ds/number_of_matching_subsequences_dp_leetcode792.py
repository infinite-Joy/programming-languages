"""

number of matching subsequences

leetcode 792

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

1st approach
    for each word is words:
        check if it is present in S

complexity : O(number of words * (size of the word + size of S))

maybe i can preprocess S and create a hashmap of the ch to the index
for each ch in words: check if this is monotonic

that way complexity is O(size of S + number of words * size of the word ))

problem is if there are duplicates in the orginal string

hence we will have to go with the 2 pointer method

we only need to find the number.  hence maybe we can implement a dp solution here

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


    a   b   c   d   e
a   1   1   1   1   1
bb  1   1   1   1   1
acd 1   1   1   2   2
ace 1   1   1   2   3

build a dp soltion like this and this is O(number of words * (size of the word + size of S))

Example :
Input:
S = "joydeep"
words = ["j", "dd, "ydp"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

        j   o   y   d   e   e   p
j       1   1   1   1   1   1   1
dd      1   1   1   1   1   1   1
ydp     1   1   1   1   1   1   2


"""

from collections import deque
from typing import List
class Solution:

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        dp = [0 for _ in range(len(S) + 1)]
        for word in words:
            word_queue = deque(list(word))
            for i, ch in enumerate(S, 1):
                incr = 0
                if word_queue and ch == word_queue[0]:
                    word_queue.popleft()
                    if not word_queue:
                        __import__('pdb').set_trace()
                        incr = 1
                    else:
                        incr = 0
                dp[i] = max(dp[i - 1], dp[i]) + incr
            print(dp)
        return dp[len(S)]


S = "abcde"
words = ["a", "bb", "acd", "ace"]
sol = Solution()
#print(sol.numMatchingSubseq(S, words))

S = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
sol = Solution()
print(sol.numMatchingSubseq(S, words))
