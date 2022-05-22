class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = 0
        for ch in s:
            if ch == letter:
                c += 1
        return int(100 * c / len(s))