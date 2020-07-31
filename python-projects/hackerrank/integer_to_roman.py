"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
27 => X + 17 => XX+7 => XXV+2 => XXVII
would probably want to implement this using segment trees
solution  = “”
numbers = [1 5 10 50 100 500 1000]
symbols = [I, V, X,  L, C, D, M]
i = len(symbols)-1
while number and i > 0:
    elem = number // numbers[i]
    if elem == 4:
        solution = solution +  symbols[i-1] + symbols[i]
    else:
solution += symbols[i]*elem
    number = number % numbers[i]
return solution


"""

class Solution:
    def intToRoman(self, num: int) -> str:
        solution = ""
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        symbols = ["I", "V", "X", "L", "C", "D", "M"]
        i = len(symbols)-1
        while num >= 0 and i >= 0:
            print(num)

            elem = num // numbers[i]
            if elem == 4:
                solution = solution + symbols[i] + symbols[i+1]
            else:
                solution += symbols[i]*elem
            num = num % numbers[i]
            i -= 1
        return solution

s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(4))
