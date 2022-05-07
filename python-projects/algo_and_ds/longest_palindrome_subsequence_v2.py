

CALLS = 0

def longest_palindrome_subsequence(arr, i, j, memo=None):
    global CALLS
    CALLS += 1
    memo = {} if memo is None else memo
    if (i, j) in memo: return memo[(i, j)]

    if i > j:
        return 0
    elif i == j:
        return 1
    elif arr[i] == arr[j]:
        memo[(i, j)] = 2 + longest_palindrome_subsequence(arr, i+1, j-1, memo)
        return memo[(i, j)]
    else:
        memo[(i, j)] = max(
            longest_palindrome_subsequence(arr, i+1, j, memo),
            longest_palindrome_subsequence(arr, i, j-1, memo)
        )
        return memo[(i, j)]


arr = "bbabcbcab"
print(arr)
print(longest_palindrome_subsequence(arr, 0, len(arr)-1))
print(CALLS)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def longest_palindrome_subsequence(arr, i, j, memo=None):
            memo = {} if memo is None else memo
            if (i, j) in memo: return memo[(i, j)]

            if i > j:
                return 0
            elif i == j:
                return 1
            elif arr[i] == arr[j]:
                memo[(i, j)] = 2 + longest_palindrome_subsequence(arr, i+1, j-1, memo)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(
                    longest_palindrome_subsequence(arr, i+1, j, memo),
                    longest_palindrome_subsequence(arr, i, j-1, memo)
                )
                return memo[(i, j)]
        return longest_palindrome_subsequence(s, 0, len(s)-1)
        