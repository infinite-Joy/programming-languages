from heapq import heapify, heappop, heappush

def sort_k_messed_array(arr, k):
  # create a heap from 0 to k + 1
  heap = arr[:k+1]
  heapify(heap)
  # print(heap)list(

  sol = []
  # start from k+2 till the end of the arr
  # keep a rolling heap
  # and insert into the heap at the same time
  for i in range(k+1, len(arr)):
    sol.append(heappop(heap))
    heappush(heap, arr[i])
    # print(heap)

  # now empty the heap and build the final parts of the sol
  while heap:
    sol.append(heappop(heap))
    # print(heap)

  return sol

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print(sort_k_messed_array(arr, k))




"""

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] k = 2
             _
       1  2   5 4 3, 7, 8, 6, 10, 9
       1  2  3  5  4 7, 8, 6, 10, 9
                4  5  7 8, 6, 10, 9

       1  2

time complexity: O(n*k)
space complexity: O(1)

second solution is using a rolling heap

time complexity: O(nlogk)
space complexity: O(k)

"""
