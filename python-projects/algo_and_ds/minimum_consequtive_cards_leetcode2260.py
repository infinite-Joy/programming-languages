"""
this can have a mapping solution which is linear time but that would have space complexity. similar to duplicate solution.

best is using a sliding window approach

"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        i = 0
        j = i
        mapping = {}
        minval = len(cards)
        outgoing = None
        incoming = None
        found = False
        while i < len(cards) and j < len(cards):
            incoming = cards[j]
            # try reducing the i and shrinking the window
            while incoming in mapping:
                found = True
                minval = min(j-i+1, minval)
                outgoing = cards[i]
                if outgoing in mapping:
                    mapping[outgoing] -= 1
                    if mapping[outgoing] == 0:
                        del mapping[outgoing]
                i += 1
            if incoming in mapping:
                mapping[incoming] += 1
            else:
                mapping[incoming] = 1
            j += 1
        return minval if found else -1