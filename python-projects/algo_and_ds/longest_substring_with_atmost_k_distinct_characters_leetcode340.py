"""

longest substring with at most k distinct characters

create your own examples

    a b c a b c a b c d e f g
                    _
                        _

    {a: 2, b: 1, c: 1, }

k = 4

bruteforce:
    is find the power set of all the distinct substrings of the string
    check if distinct chars are within k and then keep an max val.
    at the end return the max val

    complexity n2**n where n is the size of the original string. since we will need to construct the set for each k.

    space complexity: O(n)

best looks to me in 2 pointer.

    maxval: int = 0
    while fast not reached end:
        get new incoming element
        add it to the hashmap
        while set size > k:
            get outgoing element
            decrement hashmap
            if hashmap val is 0 then remove val
            increment slow
        update max
        incr fast

"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s: return 0
        if k > s: return len(s)

        slow = 0
        maxval = 0
        seen = {}
        for fast, incoming in enumerate(s):
            if incoming not in seen:
                seen[incoming] = 0
            seen[incoming] += 1
            while len(seen) > k:
                outgoing = s[slow]
                seen[outgoing] -= 1
                if seen[outgoing] == 0:
                    del seen[outgoing]
                slow += 1
            maxval = max(maxval, fast - slow + 1)
        return maxval
