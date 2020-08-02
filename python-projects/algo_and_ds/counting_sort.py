"""
# Counting sort
 Strengths:

    Linear time. Counting sort runs in O(n) time, making it asymptotically faster than comparison-based sorting algorithms like quicksort or merge sort.


 Weaknesses:

    Restricted inputs. Counting sort only works when the range of potential items in the input is known ahead of time.
    Space cost. If the range of potential values is big, then counting sort requires a lot of space (perhaps more than O(n)O(n)O(n)).

"""

from itertools import accumulate

def counter(arr, max_val):
    count_arr = [0] * (max_val+1)
    for i in arr:
        count_arr[i] += 1
    return count_arr


def build_solution(arr, count_arr):
    sol = [0] * len(arr)
    # starting from the back so as to maintain the stability of the array
    for i in arr[::-1]:
        # decrement the value to get the position
        count_arr[i] -= 1
        pos = count_arr[i]
        sol[pos] = i
    return sol


def counting_sort(arr):
    # first find the maximum of the arr
    max_val = max(arr)
    print('max_val', max_val)

    # build the counter array and accumulate
    count_arr = counter(arr, max_val)
    count_arr = list(accumulate(count_arr))
    print('count_arr', count_arr)

    # now build the solution
    return build_solution(arr, count_arr)


arr = [2,1,1,0, 2,5,4,0,2,8,7,7,9,2,0,1,9]
print(counting_sort(arr))
