"""
edit distance: find how many edits is needed to convert one string to another

first is my implementation

then there is the implementation that is based on the dynamic prgramming
time complexity is O(m*n)
space complexity is O(m*n)
"""


memo = {}

def find_del_dis(str1, str2, c=0):
  """
  Going through all the iterations and see if the deletions are present or not

  without memoisation
  time complexity: O(nm)
  space complexity: O(nm)

  using dynamic:
      time complexity O(n+m
  """
  if len(str1) == 0:
    print("finally str1 is 0")
    return c+len(str2)-1
  elif len(str2) == 0:
    print("finally str2 is 0")
    return c+len(str1)-1
  else:
    print(str1, str2, c)

    i = 0
    # in case they are matchin
    if i < len(str1) and i < len(str2):
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1

    # when they are not matching
    if (str1[i+1:], str2[i:]) in memo:
        count1 = memo[(str1[i+1:], str2[i:])]
    else:
        count1 = find_del_dis(str1[i+1:], str2[i:], c+1)
        memo[(str1[i+1:], str2[i:])] = count1
    if (str1[i:], str2[i+1:]) in memo:
        count2 = memo[(str1[i:], str2[i+1:])]
    else:
        count2 = find_del_dis(str1[i:], str2[i+1:], c+1)
        memo[(str1[i:], str2[i+1:])] = count2

    print(count1, count2)
    return min(count1, count2)

print(find_del_dis("dog", "frog"))
print(memo)
print("##################")
print("##################")
print("##################")
print("##################")
memo = {}
print(find_del_dis("heat", "hit"))
print(memo)

print("dynamic prgramming")

print(
    """
     _                             _                                                            _
    | |                           (_)                                                          (_)
  __| |_   _ _ __   __ _ _ __ ___  _  ___   _ __  _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___  _ _ __   __ _
 / _` | | | | '_ \ / _` | '_ ` _ \| |/ __| | '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
| (_| | |_| | | | | (_| | | | | | | | (__  | |_) | | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
 \__,_|\__, |_| |_|\__,_|_| |_| |_|_|\___| | .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
        __/ |                              | |               __/ |                                       __/ |
       |___/                               |_|              |___/                                       |___/

    """)


from pprint import pprint
import math


def dynamic_edit_distance(str1, str2):
    print(str1, str2)

    temp = [[math.inf for _ in range(len(str1) + 1)] for _ in range(len(str2)+1)]

    # we need same number of edits to convert the string to a null string
    # hence the first row and the first col is the same as the number
    temp[0] = [i for i in range(len(temp[0]))]
    for i, row in enumerate(temp):
        row[0] = i
    pprint(temp)

    for i, char2 in enumerate(str2, 1):
        for j, char1 in enumerate(str1, 1):
            if char1 == char2:
                # take from the diagonal
                temp[i][j] = temp[i-1][j-1]
            else:
                temp[i][j] = 1 + min(temp[i][j-1], temp[i-1][j-1], temp[i-1][j])

    pprint(temp)
    return temp[-1][-1]


print('dynamic_edit_distance("azced", "abcdef") -> ', dynamic_edit_distance("azced", "abcdef"))


def dynamic_delete_distance(str1, str2):
    print(str1, str2)

    temp = [[math.inf for _ in range(len(str1) + 1)] for _ in range(len(str2)+1)]

    # we need same number of edits to convert the string to a null string
    # hence the first row and the first col is the same as the number
    temp[0] = [i for i in range(len(temp[0]))]
    for i, row in enumerate(temp):
        row[0] = i
    pprint(temp)

    for i, char2 in enumerate(str2, 1):
        for j, char1 in enumerate(str1, 1):
            if char1 == char2:
                # take from the diagonal
                temp[i][j] = temp[i-1][j-1]
            else:
                temp[i][j] = 1 + min(temp[i][j-1], temp[i-1][j])

    pprint(temp)
    return temp[-1][-1]


print('dynamic_delete_distance("azced", "abcdef") -> ', dynamic_delete_distance("azced", "abcdef"))


def dynamic_edit_distance_without_temp(str1, str2, i, j):
    """
    This if for edit distance.
    here also i am keeping the memo and hence there is the chance this this memo might blow up
    hence space complexity is O(m*n) but with recursion
    """
    print(str1, str2, i, j)
    if i == 0:
        return j
    elif j == 0:
        return i
    else:
        if str1[i] == str2[j]:
            i = i-1
            j = j-1
            if (i, j) not in memo:
                memo[(i,j)] = dynamic_edit_distance_without_temp(str1, str2, i, j)
            return memo[(i,j)]
        else:
            left = i, j-1
            diagonal = i-1, j-1
            top = i, j-1
            if left not in memo:
                memo[left] = dynamic_edit_distance_without_temp(str1, str2, i, j-1)
            if diagonal not in memo:
                memo[diagonal] = dynamic_edit_distance_without_temp(str1, str2, i-1, j-1)
            if top not in memo:
                memo[top] = dynamic_edit_distance_without_temp(str1, str2, i-1, j)
            return 1 + min(memo[left], memo[diagonal], memo[top])

memo = {}
str1 = "azced"
str2 = "abcdef"
print('dynamic_edit_distance_without_temp("azced", "abcdef", i, j) -> ', dynamic_edit_distance_without_temp(str1, str2, len(str1)-1, len(str2)-1))
pprint(memo)


def dynamic_deletion_distance_without_temp(str1, str2, i, j):
    """
    This if for edit distance.
    here also i am keeping the memo and hence there is the chance this this memo might blow up
    hence space complexity is O(m*n) but with recursion
    """
    print(str1, str2, i, j)
    if i == 0:
        return j + 1
    elif j == 0:
        return i + 1
    else:
        if str1[i] == str2[j]:
            if (i-1, j-1) not in memo:
                memo[(i-1,j-1)] = dynamic_edit_distance_without_temp(str1, str2, i-1, j-1)
            memo[(i,j)] = memo[(i-1,j-1)]
            return memo[(i,j)]
        else:
            if (i, j-1) not in memo:
                memo[(i, j-1)] = dynamic_edit_distance_without_temp(str1, str2, i, j-1)
            if (i-1, j) not in memo:
                memo[(i-1, j)] = dynamic_edit_distance_without_temp(str1, str2, i-1, j)
            memo[(i,j)] = 1 + min(memo[(i, j-1)], memo[(i-1, j)])
            return memo[(i,j)]


memo = {}
print('dynamic_deletion_distance_without_temp("azced", "abcdef", i, j) -> ', dynamic_deletion_distance_without_temp(str1, str2, len(str1)-1, len(str2)-1))
pprint(memo)
