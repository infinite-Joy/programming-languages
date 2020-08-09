def find_pairs_with_given_difference(arr, k):
  if arr == []:
    return arr

  # create the hashset
  mapp = set(arr)

  # build the solution while checking
  solution = []
  for el in arr:
    higher = el + k
    if higher in mapp:
      solution.append([higher, el])

  return solution


arr = [0, -1, -2, 2, 1]
k = 1
print(find_pairs_with_given_difference(arr, k))






"""
arr = [0, -1, -2, 2, 1], k = 1
                     _

el = 0
y = 0 - 1 = -1
x = k + y = 1 + 0 = 1


soltion = [1,0], [0, -1], [-1, -2], [2, 1]

solution = {[-1, 0], [-2, -1], []}

time O(n)
space O(n)

"""

