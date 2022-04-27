"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

the way they are doing is using the sliding window approach for these kind of problems

abcabcbb
       _
       _

the complexity of the sliding window is O(n)
"""

from collections import defaultdict, deque


def longest_substrings(string):
    i = 0
    j = 0
    curr = deque([])
    max_string = []
    max_count = 0
    counts = defaultdict(int)
    for j in range(len(string)):
        incoming = string[j]
        curr.append(incoming)
        counts[incoming] += 1
        while i <= j:
            if counts[incoming] > 1:
                i += 1
                outgoing = curr.popleft()
                counts[outgoing] -= 1
            else: # that means that this is a valid string
                # update the max values
                max_count = max(max_count, len(curr))
                if max_count == len(curr):
                    max_string = curr
                # we also need to come out of the loop
                break
    return max_count

print(longest_substrings('abcabcbb'))
print(longest_substrings('bbbbb'))
