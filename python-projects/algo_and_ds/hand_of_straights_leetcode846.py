"""
we will keep a hashmap of the last entries and the arr of arrs:
1    2    3    6    2    3    4    7    8
hashmap: {last entry: (pos, size)}
[[1]], {1: (0, 1)}
check if incoming - 1 present in the hashmap and the size is less than W
if yes remove that entry and shift it to the new value
[[1, 2]] , {2, (0, 2)}
incoming = 3
[[1,2,3]], {3:(0, 3)}
incoming 6
[[1,2,3], [6]] {3:(0, 3)} {6:(1, 1)}
incoming 2
[[1,2,3], [6], [2]] {3:(0, 3), 6:(1, 1), 2: (2, 1)
incoming 3
[[1,2,3], [6], [2, 3]] {3:(0, 3), 6:(1, 1), 3: (2, 2)
===================================
class Solution:
def isNStraightHand(self, hand: List[int], W: int) -> bool:
    newhand = []
    enders_hm = {}
    minval = 0
    for card in hand:
        if card - 1 in enders_hm and enders_hm[card - 1][1] < W:
            pos, oldsize = enders_hm[card - 1]
            del enders_hm[card - 1]
            newhand[pos].append(card)
            enders_hm(card) = (pos, oldsize + 1)
            minval = min(minval, oldsize + 1)
        else:
            present_size = len(newhand)
            newhand.append([card])
            enders_hm[card] = (present_size, 1)
minval = min(minval, 1)
    if minval < W:
        return False
    return True


"""
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        newhand = []
        enders_hm = {}
        starters_hm = {}
        for card in hand:
            if card - 1 in enders_hm and len(newhand[enders_hm[card - 1]]) < W:
                pos = enders_hm[card - 1]
                del enders_hm[card - 1]
                newhand[pos].append(card)
                enders_hm[card] = pos
            elif card + 1 in starters_hm and len(newhand[starters_hm[card + 1]]) < W:
                pos = starters_hm[card + 1]
                del starters_hm[card + 1]
                newhand[pos].append(card)
                starters_hm[card] = pos
            else:
                present_size = len(newhand)
                newhand.append([card])
                enders_hm[card] = present_size
                starters_hm[card] = present_size
            print(newhand, starters_hm, enders_hm)

        if min(len(x) for x in newhand) < W:
            return False
        return True

hand = [1,2,3,6,2,3,4,7,8]
W = 3
sol = Solution()
#print(sol.isNStraightHand(hand, W))

hand = [2,1]
W = 2
sol = Solution()
print(sol.isNStraightHand(hand, W))
