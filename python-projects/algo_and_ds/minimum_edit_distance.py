"""
memoisation makes this from exponental to 
"""



def minimum_edit_distance(src, target, i, j, memo=None):
    memo = {} if memo is None else memo
    if (i, j) in memo: return memo[(i, j)]

    print(i, j)
    # base case
    if i == j == -1:
        return 0
    if j == -1:
        return i
    if i == -1:
        return j
    else:
        if src[i] == target[j]:
            memo[(i, j)] = minimum_edit_distance(src, target, i-1, j-1, memo)
            return memo[(i, j)]
        else:
            memo[(i, j)] = min(
                1 + minimum_edit_distance(src, target, i, j-1, memo),
                1 + minimum_edit_distance(src, target, i-1, j, memo),
                2 + minimum_edit_distance(src, target, i-1, j-1, memo),
            )
            return memo[(i, j)]

from pprint import pprint

def minimum_edit_distance(src, target):
    firsttable = [0 for _ in range(len(target) + 1)] # target x src
    table = [firsttable[::] for _ in range(len(target) + 1)]
    # this is for if the target is empty
    for i in range(len(src)):
        table[0][i+1] = table[0][i] + 1
    # this is for if the src is empty
    for j in range(len(target)):
        table[j+1][0] = table[j][0] + 1
    pprint(table)

    for j, tch in enumerate(target, start=1):
        for i, sch in enumerate(src, start=1):
            if tch == sch:
                table[j][i] = table[j-1][i-1]
            else:
                table[j][i] = min(
                    1 + table[j][i-1], 2 + table[j-1][i-1], 1 + table[j-1][i]
                )
    pprint(table)
    print(table[-1][-1])

    

source = 'ABCDEFG'
target = 'ABDFFGH'
# print(minimum_edit_distance(source, target, len(source)-1, len(target)-1))
print(minimum_edit_distance(source, target))