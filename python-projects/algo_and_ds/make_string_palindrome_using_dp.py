"""

https://www.careercup.com/question?id=6287528252407808

the distance between two strings

deletions to make the string palindromic

abcdba

    a   b   c   d   b   a
a   0   1   2   3   4   5
b   0   0   1   2   3   4
d   0   0   2   1   2   3
c   0   0   2   2   1   2
b   0   0   2   2   2   3
a   0   0   2   2   2   2

edit distance recurrent = min(dp[i-1][j-1] + if a == b then 0 else 1, dp[i-1][j]+1, dp[i][j-1] + 1)

i will write the code for n2 and leave it at that

"""

def edit_distance(string1, string2):
    print(string1, string2)
    n = len(string1)

    # initialise the dp
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # edit distance between a null string and any other string is the length
    # of the other string
    dp[0] = [i for i in range(n+1)]
    print(dp[0])

    # build up the dp table
    for i, ch1 in enumerate(string1, 1):
        for j, ch2 in enumerate(string2, 1):
            #__import__('pdb').set_trace()
            adder = 1
            if ch1 == ch2:
                adder = 0
            dp[i][j] = min(dp[i-1][j-1] + adder, dp[i-1][j] + 1, dp[i][j-1] + 1)
        print(dp[i])

    return dp[n][n]

def k_palindrome(string, k):
    distance = edit_distance(string, string[::-1])
    if distance <= 2 * k:
        return True
    return False

print(k_palindrome('abxa', 1))
print(k_palindrome('abdxa', 1))
print(k_palindrome('abaxbabax', 1))
