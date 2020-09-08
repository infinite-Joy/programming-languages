"""

number of matching subsequences

leetcode 792

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

the previous soltuon did not work

so we will create a list of list of queues
and for each letter we will put them into the respective queues

"""

from typing import List
from collections import deque
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        queues = [[] for _ in range(ord('a'), ord('z') + 2)] # last one is for none
        for word in words:
            firstletter = word[0]
            queues[ord(firstletter) - ord('a')].append(deque(word[1:]))
        print(queues)

        for ch in S:
            pos = ord(ch) - ord('a')
            if queues[pos]:
                # get the queues
                pos_queues = queues[pos]
                # reset pos
                queues[pos] = []
                # reassign the queues again to the respective locations
                for queue in pos_queues:
                    if queue:
                        next_ch = queue.popleft()
                        queues[ord(next_ch) - ord('a')].append(queue)
                    else:
                        queues[-1].append(queues)
                print(queues)



        return len(queues[-1])


S = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
sol = Solution()
print(sol.numMatchingSubseq(S, words))


