# https://leetcode.com/problems/minimum-window-substring/


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        using the 2 pointer method

        saving the min value that is see so far

        """
        t = Counter(t)
        summ = sum(v for _, v in t.items())
        i = 0
        j = 0
        minlen = len(s)
        min_window = ""
        curr_set = {}
        curr_sum = 0
        while j < len(s):
            print(i, j, s[i], s[j])
            if len(curr_set) == len(t) and curr_sum == summ:
                # checking and updating the min string
                minlen = min(minlen, j - i + 1)
                if minlen == (j - i + 1):
                    min_window = s[i:j+1]

                if s[i] in curr_set:
                    curr_set[s[i]] -= 1
                    curr_sum -= 1
                    if curr_set[s[i]] == 0:
                        del curr_set[s[i]]
                i += 1
            else:
                if s[j] in t:
                    if s[j] not in curr_set:
                        curr_set[s[j]] = 0
                    curr_set[s[j]] += 1
                    curr_sum += 1
                j += 1
            print(curr_set)
        while i < len(s):
            #__import__('pdb').set_trace()
            if len(curr_set) == len(t) and curr_sum == summ:
                # checking and updating the min string
                minlen = min(minlen, j - i)
                if minlen == (j - i):
                    min_window = s[i:j]

                if s[i] in curr_set:
                    curr_set[s[i]] -= 1
                    if curr_set[s[i]] == 0:
                        del curr_set[s[i]]
            i += 1
        return min_window

S = "ADOBECODEBANC"
T = "ABC"
sol = Solution()
#print(sol.minWindow(S, T))
#Output: "BANC"

S = "a"
T = "a"
sol = Solution()
print(sol.minWindow(S, T))

S = "a"
T = "aa"
sol = Solution()
print(sol.minWindow(S, T))
