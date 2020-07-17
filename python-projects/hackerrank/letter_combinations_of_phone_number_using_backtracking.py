"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
probably something like that
take the  previous
do a for loop on the current
and then pass it on the next
====================================================================================

time complexity: O(n)
space complexity: O(n)

"""

from typing import Dict, List


def build_letter_combs(
        digits: str, mapping: Dict[str, List[int]], previous: str, this: int):
    """
    Args:
        digits: the digits
        mapping: the mapping of numbers to strings
        previous: the previous build till now
        this: the current digits that is being considered
    Returns:
        full completed string
    """
    if this == len(digits):
        yield previous
    else:
        #print(digits, mapping, previous, this)
        digits_char = int(digits[this])
        chars = mapping[digits_char]
        if chars is not None:
            for ch in chars:
                till_now = previous + ch
                next_level = this + 1
                yield from build_letter_combs(digits, mapping, till_now, next_level)


def letter_combs(digits):
    mapping = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    solution = []
    for s in build_letter_combs(digits, mapping, "", 0):
        solution.append(s)
    return solution

print(letter_combs("23"))
