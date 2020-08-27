"""

https://www.careercup.com/question?id=4909367207919616

WAP to modify the array such that arr[I] = arr[arr[I]].
Do this in place i.e. with out using additional memory.

example : if a = {2,3,1,0}
o/p = a = {1,0,3,2}

Note : The array contains 0 to n-1 integers.

arr[0] = 1
arr[arr[1]] = arr[0] = 1

2   3   1   0
    _
1   3   2   0
2

=================

    2   4   3   1   0
        _
    3   4   2   1   0
    3   0   2   1   4
    3   0   2   1   4
    3   1   2   0   4

time complexity: O(n)
space complexity: O(1)

"""

def wap(arr):
    for i in range(len(arr)):
        val = arr[i]
        arr[i], arr[val] = arr[val], arr[i]


arr = [2,3,1,0]
wap(arr)
print(arr)


arr = [2,4,3,1, 0]
wap(arr)
print(arr)

