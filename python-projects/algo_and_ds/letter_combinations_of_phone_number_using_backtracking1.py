"""
letter combinations of phone number using backtracking

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

here we can start with the first letter then go to the nect letter and so on

the complexity is 4**n

assumptionsL gitis will be less

"""

mapping = {
    '1': '',
    '0': ' ',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def letter_combinations(digits, comb=None):
    if not digits:
        if comb:
            yield "".join(comb)
        else:
            yield ""
        return

    curr = digits[0] # 2, 3
    for ch in mapping[curr]: # 'a', d
        comb.append(ch) # [ad]
        yield from letter_combinations(digits[1:], comb) # (3, [a]), ('', [ad]), 
        comb.pop()

def main(digits):
    for comb in letter_combinations(digits, comb=[]):
        if comb:
            print(comb)
    print('#'*50)

# test case
main('23')
main('')