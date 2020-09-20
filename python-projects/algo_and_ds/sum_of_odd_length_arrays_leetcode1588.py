"""
sum of odd length subarrays
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


    1   5   7   12  15
1   1   5   7   12  15
4   1   5   0   0   0
2   1   5   14  0   0
5   1   5   14  30  0
3   1   5   14  30

S3 = (s2 + i) +

S1 = 0 + s1
s2 = s1 + i
s3 = 2(sum2 + i)
s4 = (sum3 + i) + sum3 + (sum3 - outgoing + i)
s5 = (sum4 + i) +

this is complicated. can i do a prefix sum

    1   4   2   5   3   3

    1   5   7   12  15  18
    15  14  10  8    3

    1   5   7   12  15
    1   6   14  30  58  89

going back to the n2 solution


"""

#first solution. this is O(n2) not good.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i) % 2 == 0:
                    summ += sum(arr[i:j+1])
        return summ



# doing this in O(n)
"""

    arr = [1,4,2,5,3]

            1   5   7   12  15
            1   6   14  30  58  89

            1,1

"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_even_counts = [0, 0]
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i) % 2 == 0:
                    summ += sum(arr[i:j+1])
        return summ
