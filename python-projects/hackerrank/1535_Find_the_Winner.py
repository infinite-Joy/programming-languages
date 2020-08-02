"""
this looks like a 2 pointer method

we take i and j and then check for each i if there are anything that is greater than i in i+k
if there is something there then we update the. i

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2

"""

from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        j = 0
        winner = 0
        while j < len(arr) and j - i <= k:
            # print(i, j, arr[i], arr[j])
            if j > i:
                if arr[j] >= arr[winner]:
                    winner = j
                    i += 1
            j += 1
        return arr[winner]

    def getWinner(self, arr, k):
        curr = arr[0]
        win = 0
        for item in arr[1:]:
            if item > curr:
                curr = item
                win = 0
            win += 1
            if win == k:
                return curr
        return curr


s = Solution()

arr = [2,1,3,5,4,6,7]
k = 2
print(s.getWinner(arr, k))

arr = [3,2,1]
k = 10
print(s.getWinner(arr, k))

arr = [1,9,8,2,3,7,6,4,5]
k = 7
print(s.getWinner(arr, k))

arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000
print(s.getWinner(arr, k))

arr = [1,25,35,42,68,70]
k = 1
print(s.getWinner(arr, k)) # answer = 25
