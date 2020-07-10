from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Get the longest substring
        Args:
            s: the input string
        Returns:
            int, the size of the longest substring
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        i = 0
        j = 1
        counts = defaultdict(int)
        ch = s[i]
        counts[ch] = 1
        max_len = 0
        while j < len(s):

            #__import__('pdb').set_trace()

            ch = s[j]
            counts[ch] += 1

            if counts[ch] > 1:
                while counts[ch] > 1:
                    ch1 = s[i]
                    counts[ch1] -= 1
                    i += 1

            max_len = max(max_len, j-i+1)

            j += 1
        return max_len

print(Solution().lengthOfLongestSubstring("abcabcbb"))
