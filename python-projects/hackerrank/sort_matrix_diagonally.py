"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
we can go from bottom-left to top-left to top-right.
get the diagonal array and sort them out
time complexity is O(n+m)logn
space complexity is O(n)
============================================================================
"""
from pprint import pprint


def build_diagonal(matrix, x, y):
    indices = []
    j = 0
    while x+j < len(matrix) and y+j < len(matrix[0]):
        indices.append((x+j, y+j))
        j += 1
    return indices


def merge(matrix, x1, y1, x2, y2, midx, midy):
    i = 0
    j = 0
    while x1+i<midx and midx+j<=x2:
        if matrix[x1+i][y1+i] <= matrix[midx+i][midy+j]:
            i += 1
        else:
            matrix[x1+i][y1+i], matrix[midx+i][midy+j] = matrix[midx+i][midy+j], matrix[x1+i][y1+i]
            j += 1


def merge_sort(matrix, x1, y1, x2, y2):
    import time; time.sleep(1)
    print(x1, y1, x2, y2)
    if x2<=x1:
        return
    elif y2<=y1:
        return
    else:
        midx = (x1 + x2) // 2
        midy = (y1 + y2) // 2
        print('after calc',x1, y1, x2, y2,midx, midy)
        merge_sort(matrix, x1, y1, midx, midy)
        merge_sort(matrix, midx, midy, x2, y2)
        merge(matrix, x1, y1, x2, y2, midx, midy)


mat = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]
mat = merge_sort(mat, 0, 0, 2, 2)
pprint(mat)


def find_diagonal(matrix):
    for i in range(len(matrix)):
        diagonals = [x for x in build_diagonal(matrix, i, 0)]
        merge_sort(matrix, diagonals[0][0], diagonals[0][1], diagonals[-1][0], diagonals[-1][1])
    for i in range(1, len(matrix[0])):
        diagonals = [x for x in build_diagonal(matrix, 0, i)]
        merge_sort(matrix, diagonals[0][0], diagonals[0][1], diagonals[-1][0], diagonals[-1][1])
    return matrix

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
mat = find_diagonal(mat)
pprint(mat)

