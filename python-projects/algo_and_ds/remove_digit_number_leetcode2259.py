"""
This is an O(n) solution.

similar to how you run running hash

"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        leftval = int(number)
        rightval = 0
        maxval = 0
        for i in range(len(number)):
            ch = number[len(number)-1-i]
            leftval = leftval - (int(ch) * (10 ** i))
            if ch == digit:
                maxval = max(maxval, rightval + (leftval // 10))
            rightval = rightval + (int(ch) * (10 ** i))
            # print(f'{leftval=}')
            # print(f'{rightval=}')
        return str(int(maxval))