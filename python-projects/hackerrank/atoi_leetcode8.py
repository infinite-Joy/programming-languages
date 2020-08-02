"""

https://leetcode.com/problems/string-to-integer-atoi/
this can be done using the
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

can do with simple getting the number
complexity is O(n)
=====================================
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        whitespace = True
        minint = -2**31
        maxint = 2**31
        number = 0
        negative = False
        positive = False
        while i < len(str):
            if str[i] != ' ' and whitespace is True:
                whitespace = False
            if whitespace is False and str[i] == '-':
                if positive is not True:
                    negative = True
                else:
                    return 0
            if whitespace is False and str[i] == '+':
                if negative is not True:
                    positive = True
                else:
                    return 0
            if whitespace is False:
                if positive is True or (str[i] >= '0' or str[i] <= '9'):
                    if positive is True and str[i] != '+':
                        number = number*10 + int(str[i])
                else:
                    return number
                if negative is True and (str[i] >= '0' or str[i] <= '9'):
                    if negative is True and str[i] != '-':
                        number = number*10 - int(str[i])
                    if negative is False:
                        number = number*10 + int(str[i])
                    if number < minint:
                        return minint
                    if number > maxint:
                        return maxint
                else:
                    return number
            i+=1
        return number

s = Solution()
assert s.myAtoi("42") == 42
assert s.myAtoi("    -42") == -42
assert s.myAtoi("4193 with words") == 4193
assert s.myAtoi("3.14159") == 3
assert s.myAtoi("+1") == 1
