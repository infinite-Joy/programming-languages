"""

Microsoft Excel numbers cells as 1...26 and after that AA, AB.... AAA, AAB...ZZZ and so on.

Given a number, convert it to that format and vice versa.

encoder and decoder

26*1, 26**2, 26***3

first find the power for which

and then once the power is there then do the division and find the

576 = 5 * 10**2 +

"""

from string import ascii_letters

def encode(num): # 728
    letters = ascii_letters[:26]
    sol = []
    while num > 0:
        sol.append(num % 26)
        num = (num - 1) // 26
    sol.reverse()
    return sol

num = 1
print(encode(num))

num = 28
print(encode(num))

num = 701
print(encode(num))
