# next smallest palindrome

"""
check the next smallest palindrome

method 1:

increment the number by 1 and check if this is a palindrome

complexity: n2

method 2: thinking as a graph problem

keep the first one, or keep the second one and then keep going inside

complexity. 2**(n/2) where n is the number of digits. == log(x)

we can do this using backtracking

23545
    23542
        23532
        24542
    53545

backtracking did not work.

here is the solution https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

explanation https://www.youtube.com/watch?v=hZcindWcYI4


"""

def ispalindrom(n):
    nstr = str(n)
    return nstr == nstr[::-1]

def simple_palindrome(num):
    start = 1
    num1 = 0
    for digit in num[::-1]:
        num1 += digit * start
        start *= 10
    notfound = True
    num = num1
    while notfound:
        num += 1
        if ispalindrom(num):
            notfound = False
    return num

print(simple_palindrome([2,3,5,4,5]))


def check_palindrome(num):
    return num == num[::-1]

print(check_palindrome([1,2,1]))

def minimum(num1, num2):
    for n1, n2 in zip(num1, num2):
        if n1 != n2:
            if min(n1, n2) == n1:
                return num1
            else:
                return num2
    else:
        return num1

print(minimum([1,2,3], [1,2,4]))



def explore(num, movement, mov_limit):
    if movement >= mov_limit:
        return num[:]

    left_num = num[movement]
    right_num = num[len(num) - 1 - movement]
    left_is_palindrome = right_is_palindrom = None

    # keep left
    num[len(num) - 1 - movement] = left_num
    left_is_palindrome = check_palindrome(num)
    if left_is_palindrome:
        next_palindrome_num_left = num[:]
    else:
        next_palindrome_num_left = explore(num, movement+1, mov_limit)
    num[len(num) - 1 - movement] = right_num

    # keep right
    num[movement] = right_num
    right_is_palindrom = check_palindrome(num)
    if right_is_palindrom:
        next_palindrome_right = num[:]
    else:
        next_palindrome_right = explore(num, movement+1, mov_limit)

    return minimum(next_palindrome_num_left, next_palindrome_right)




def next_palindrome(num):
    movement = 0
    mov_limit = int(len(num) / 2)
    return explore(num, movement, mov_limit)



print(next_palindrome([2,3,5,4,5]))