"""

https://leetcode.com/contest/weekly-contest-294/problems/sum-of-total-strength-of-wizards/

"""


def divide_and_conquer(strength, i, j):
    if i == j:
        return strength[i] * strength[i], strength[i], strength[i] # sum, min, normalsum
    else:
        mid = (i+j) // 2
        leftsum, leftmin, left_nsum = divide_and_conquer(strength, i, mid)
        rightsum, rightmin, right_nsum = divide_and_conquer(strength, mid+1, j)
        
        thismin = min(leftmin, rightmin)
        thissum = thismin * (left_nsum+right_nsum) + leftsum + rightsum
        return thissum, thismin, left_nsum+right_nsum
    



# strength = [5,4,6]
strength = [5, 4, 6]
ans = divide_and_conquer(strength, 0, len(strength)-1)
print('25 + 16 + 4*9', 25 + 16 + 4*9)
print(ans, 'actual', 213)

# this is not working