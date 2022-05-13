"""
spiral order using rotation
"""


def spiral_order(mat, top, left, bottom, right):
    print(top, left, bottom, right)
    out = []
    if top <= bottom and left <= right:
        i = top
        j = left
        # go right
        for j in range(left, right+1):
            out.append(mat[i][j])
        # go down
        for i in range(top+1, bottom+1):
            out.append(mat[i][j])
        # go left
        if top < bottom:
            for j in range(right-1, left-1, -1):
                out.append(mat[i][j])
        # go up
        if right > left:
            for i in range(bottom-1, top, -1):
                out.append(mat[i][j])
        print(out)
        inner = spiral_order(mat, top+1, left+1, bottom-1, right-1)
        out.extend(inner)
    return out

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(spiral_order(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1))

    # 1   2   3   4
    # 5   6   7   8
    # 9   10  11  12

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_order(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1))
# print(spiral_order(matrix, 1, 1, 1, 2))
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6]


"""
do this in a recursive application


"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral_order(mat, top, left, bottom, right):
            # print(top, left, bottom, right)
            out = []
            if top <= bottom and left <= right:
                i = top
                j = left
                # go right
                for j in range(left, right+1):
                    out.append(mat[i][j])
                # go down
                for i in range(top+1, bottom+1):
                    out.append(mat[i][j])
                # go left
                if top < bottom:
                    for j in range(right-1, left-1, -1):
                        out.append(mat[i][j])
                # go up
                if right > left:
                    for i in range(bottom-1, top, -1):
                        out.append(mat[i][j])
                # print(out)
                inner = spiral_order(mat, top+1, left+1, bottom-1, right-1)
                out.extend(inner)
            return out
        return spiral_order(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1)