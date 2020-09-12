"""

decode string

leetcode 394

                        3[a2[c]]
                    a2[c]
                c

time complexity: O(n)
space complexity: O(n)

"""

from string import ascii_letters

class Solution:
    def helper(self, count, s, i, len):
        string_builder = []
        while i < len:
            if s[i] in ascii_letters:
                string_builder.append(s[i])
                i += 1
            elif s[i].isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                if s[i] == '[':
                    string, i = self.helper(num, s, i + 1, len)
                    string_builder.extend(string)
            elif s[i] == ']':
                return count * string_builder, i + 1
        return count * string_builder, i + 1

    def decodeString(self, s: str) -> str:
        if not s: return s
        string, _ = self.helper(1, s, 0, len(s))
        return "".join(string)

# test case
s = "3[a]2[bc]"
sol = Solution()
print(sol.decodeString(s))

s = "3[a2[c]]"
sol = Solution()
print(sol.decodeString(s))
