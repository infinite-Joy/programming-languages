"""

find the longest palindrome

using expand around center

time complexity is O(n2)
and space complexity is O(1) removing the need for the solution string or i can return the indices

"""

def expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        print(left, right)
        left -= 1
        right += 1
    return right - left - 1, left + 1, right - 1

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return ""
        string = s
        maxval = 0
        greatestindex = 0
        for i, _ in enumerate(string):
            #__import__('pdb').set_trace()
            oddlen, *_ = expand_around_center(string, i, i)
            evenlen, *_ = expand_around_center(string, i, i+1)
            maxval = max(oddlen, evenlen, maxval)
            print(oddlen, evenlen, maxval)
            # if maxval has been updated then update the greatestindex as well
            if maxval == oddlen or maxval == evenlen:
                greatestindex = i
        # now find the left and right to the greeatest index
        oddlen, oddleft, oddright = expand_around_center(string, greatestindex, greatestindex)
        evenlen, evenleft, evenright = expand_around_center(string, greatestindex, greatestindex + 1)
        if oddlen >= evenlen:
            return string[oddleft:oddright+1]
        else:
            return string[evenleft:evenright+1]

s = Solution()
string = 'babab'
print(string)
print(s.longestPalindromeSubseq(string))

string = 'babad'
print(string)
print(s.longestPalindromeSubseq(string))
