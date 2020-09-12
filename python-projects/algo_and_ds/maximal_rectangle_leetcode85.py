"""

maximal rectangle

this is a dp solution

basically from teh upper bound to thhe lower bound

basically for all cells, if the cell is not covered
    take the next row and see if this is a rectangle
    take the next col and see if this is a rectangle
    take the diagonal and see if this is a rectangle
    update the lowerbound upper bound rectangle size


Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

in this way we get time complexity: O(number of rows * number of cols)
space complexity: O(size of row * size of col)

"""

from typing import List
class Solution:
    def curr_rectangle(self, matrix, ubrow, ubcol, lbrow, lbcol, rectangles):
        print(ubrow, ubcol, lbrow, lbcol, rectangles)
        # col expansion
        col_exp_true = True
        if (lbcol + 1) < len(matrix[0]):
            for row in range(ubrow, lbrow + 1):
                if matrix[row][lbcol + 1] != "1":
                    col_exp_true = False
            if col_exp_true is True:
                rectangles[(ubrow, ubcol, lbrow, lbcol + 1)] = rectangles[(ubrow, ubcol, lbrow, lbcol)] + (lbrow - ubrow + 1)
                self.curr_rectangle(matrix, ubrow, ubcol, lbrow, lbcol + 1, rectangles)

        # row expansion
        row_exp_true = True
        if (lbrow + 1) < len(matrix):
            for col in range(ubcol, lbcol + 1):
                if matrix[lbrow + 1][col] != "1":
                    row_exp_true = False
            if row_exp_true is True:
                rectangles[(ubrow, ubcol, lbrow + 1, lbcol)] = rectangles[(ubrow, ubcol, lbrow, lbcol)] + (lbcol - ubcol + 1)
                self.curr_rectangle(matrix, ubrow, ubcol, lbrow + 1, lbcol, rectangles)

        # diagonal expansion
        if (lbrow + 1) < len(matrix) and (lbcol + 1) < len(matrix[0]) and row_exp_true and col_exp_true:
            if matrix[lbrow + 1][lbcol + 1] == '1':
                rectangles[(ubrow, ubcol, lbrow + 1, lbcol + 1)] = rectangles[(ubrow, ubcol, lbrow, lbcol + 1)] + rectangles[(ubrow, ubcol, lbrow + 1, lbcol)] - rectangles[(ubrow, ubcol, lbrow, lbcol)] + 1
                self.curr_rectangle(matrix, ubrow, ubcol, lbrow + 1, lbcol + 1, rectangles)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # rectangles will have upper bound, lower bound as key and size as value
        # this will be the dp
        rectangles = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    rectangles[(row, col, row, col)] = 1
                    self.curr_rectangle(matrix, row, col, row, col, rectangles)
        return max(rectangles.values())
class Solution:
    def curr_rectangle(self, matrix, ubrow, ubcol, lbrow, lbcol, rectangles):
        print(ubrow, ubcol, lbrow, lbcol, rectangles)
        # col expansion
        if (lbcol + 1) < len(matrix[0]):
            if ubrow == lbrow or ((ubrow, ubcol, lbrow, lbcol) in rectangles and (ubrow, ubcol, lbrow - 1, lbcol + 1) in rectangles):
                if matrix[lbrow][lbcol + 1] == "1":
                    rectangles[(ubrow, ubcol, lbrow, lbcol + 1)] = rectangles[(ubrow, ubcol, lbrow, lbcol)] + (lbrow - ubrow + 1)
                    self.curr_rectangle(matrix, ubrow, ubcol, lbrow, lbcol + 1, rectangles)

        # row expansion
        if (lbrow + 1) < len(matrix):
            if ubcol == lbcol or ((ubrow, ubcol, lbrow, lbcol) in rectangles and (ubrow, ubcol, lbrow + 1, lbcol - 1) in rectangles):
                if matrix[lbrow + 1][lbcol] == "1":
                    rectangles[(ubrow, ubcol, lbrow + 1, lbcol)] = rectangles[(ubrow, ubcol, lbrow, lbcol)] + lbcol - ubcol + 1
                    self.curr_rectangle(matrix, ubrow, ubcol, lbrow + 1, lbcol, rectangles)

        # diagonal expansion
        if (lbrow + 1) < len(matrix) and (lbcol + 1) < len(matrix[0]) and (ubrow, ubcol, lbrow, lbcol + 1) in rectangles and (ubrow, ubcol, lbrow + 1, lbcol) in rectangles and (ubrow, ubcol, lbrow, lbcol) in rectangles:
            if matrix[lbrow + 1][lbcol + 1] == '1':
                rectangles[(ubrow, ubcol, lbrow + 1, lbcol + 1)] = rectangles[(ubrow, ubcol, lbrow, lbcol + 1)] + rectangles[(ubrow, ubcol, lbrow + 1, lbcol)] - rectangles[(ubrow, ubcol, lbrow, lbcol)] + 1
                self.curr_rectangle(matrix, ubrow, ubcol, lbrow + 1, lbcol + 1, rectangles)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # rectangles will have upper bound, lower bound as key and size as value
        # this will be the dp
        rectangles = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    rectangles[(row, col, row, col)] = 1
                    self.curr_rectangle(matrix, row, col, row, col, rectangles)
        return max(rectangles.values())

# test case
arr = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
sol = Solution()
print(sol.maximalRectangle(arr))

arr = [["0"]]
sol = Solution()
print(sol.maximalRectangle(arr))
