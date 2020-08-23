"""
[8, 10, 2]

for first index iterate through the arr and find the product

 i
[8, 10, 80]

arr = [2, 7, 3, 4]

first run [1, 2, 14, 42] cumulative product build
back run [84 12 4 1]

second run [84 24 56 42] going from the back

time complexity O(n)
sopace O(n)

"""


def array_of_array_products(arr):
  if len(arr) == 0 or len(arr) == 1:
    return []

  # forward run
  forward = [1]
  for item in arr[:-1]:
    forward.append(item*forward[-1])

  # backward run
  backward = [1]
  for item in list(reversed(arr))[:-1]:
    backward.append(item*backward[-1])
  backward = backward[::-1]

  return [x*y for x, y in zip(forward, backward)]


arr = [2, 7, 3, 4]
print(array_of_array_products(arr))

arr = [8, 10, 2]
print(array_of_array_products(arr))

arr = []
print(array_of_array_products(arr))

arr = [2]
print(array_of_array_products(arr))

