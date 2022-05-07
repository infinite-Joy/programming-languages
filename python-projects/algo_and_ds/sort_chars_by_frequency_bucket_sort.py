"""
This can be done using bucket sort

the higest count will be total size of the numbers.

ebcause you can assign the numbers to the different buckets and then sort the numbers.

this is not a stable sort though. you cannot know which one came first

since the amount of space used is constant. space O(1)

time complexity: O(n)

"""

import string

class Solution:
    def frequencySort(self, s: str) -> str:
        chars = string.ascii_letters + string.digits
        mapping = {ch: i for i, ch in enumerate(chars)}
        buckets = [[0, i] for i in range(len(chars))]
        for ch in s:
            buckets[mapping[ch]][0] += 1
        buckets.sort(key=lambda x: x[0], reverse=True)
        soln = []
        for c, idx in buckets:
            if c > 0:
                thisbuild = chars[idx] * c
                soln.append(thisbuild)
        return "".join(soln)