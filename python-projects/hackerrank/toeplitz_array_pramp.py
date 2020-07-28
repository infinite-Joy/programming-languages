"""
def happy_mat(mat):


A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]

is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

isn’t a Toeplitz matrix, so we should return false.

time complexity is O(n)
space is O(1)
"""

#def run_diagonal(arr, diag_row, diag_col)


def isToeplitz(arr):
  """
  @param arr: int[][]
  @return: bool
  """
  no_rows = len(arr)
  no_cols = len(arr[0])

  # from left bottom to left top
  for row in range(no_rows-1, -1, -1):
    diag_row, diag_col = row, 0
    val = arr[diag_row][diag_col]
    while diag_row < no_rows and diag_col < no_cols:
      if val == arr[diag_row][diag_col]:
        diag_row, diag_col = diag_row+1, diag_col+1
      else:
        return False

  # from left top to top right
  for col in range(1, no_cols):
    diag_row, diag_col = 0, col
    val = arr[diag_row][diag_col]
    while diag_row < no_rows and diag_col < no_cols:
      if val == arr[diag_row][diag_col]:
        diag_row, diag_col = diag_row+1, diag_col+1
      else:
        return False

  return True


arr = [[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
print(isToeplitz(arr))

arr = [[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

print(isToeplitz(arr))

"""
  try to run the code


  you can traverse given matrix diagonaly

 probably that would be simpler. traversing diagonally. but thinking about how to do that
  would probably take up too much time for me right now
  ok your approch is also good but as th
 or rather let me try

 you think i should try diagonally or
  better the rabin karp one?
  if you are asking me then i'll prefer to go with diagonal because it take O(n)time and O(1) space complexity

  ok
  let me try to get the diagonal one

  algo
  start from the

  n = len(mat)
  start from the bottom left and go diagonal as long as there is an entry
    next diagonal is given by [row+1][col+1]. makes sense?
    if it makes sense I will go ahead and write the code


    ok right like that writ eit


 ok so

"""

def is_toeplitz(mat):
    rollinghash1 = 0
    rollinghash2 = 0
    prev_rollinghash1 = None
    for row in range(len(mat)):
        #print(mat[row])
        for col in range(len(mat[0])):
            #__import__('pdb').set_trace()

            if col == 0: # first elem
                rollinghash1 = 10*rollinghash1 + mat[row][col]
                rollinghash2 = 0

            elif mat[row][-1] == mat[row][col]: # if last element
                rollinghash2 = 10*rollinghash2 + mat[row][col]
                if row!=0 and rollinghash2 != prev_rollinghash1:
                    return False
                prev_rollinghash1 = rollinghash1
                rollinghash1 = 0

            else:
                rollinghash1 = 10*rollinghash1 + mat[row][col]
                rollinghash2 = 10*rollinghash2 + mat[row][col]

            #print(rollinghash1, rollinghash2, prev_rollinghash1)

    return True

arr = [[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
print(is_toeplitz(arr))

arr = [[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

print(is_toeplitz(arr))
