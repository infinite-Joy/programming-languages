"""
integer to roman can be done using a tree

this looks like a brute force.

more than a tree probably a greedy solution would work

"""


def intToRoman(num: int) -> str:
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ''
    for number, symbols in zip(numbers, symbols):
        # print(num, number, symbols)
        while num and num >= number:
            repeat = int(num / number)
            num = num % number
            roman = roman + symbols*repeat
        if num == 0:
            return roman
    return roman

# print(intToRoman(1))
# print(intToRoman(2))
print(intToRoman(4))
# print(intToRoman(8))
# print(intToRoman(16))
# print(intToRoman(32))
# print(intToRoman(64))
# print(intToRoman(132))