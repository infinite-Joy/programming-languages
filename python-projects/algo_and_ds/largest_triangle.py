"""
https://www.hackerrank.com/challenges/largest-rectangle/problem
10 6320 6020 6098 1332 7263 672 9472 28338 3401 9494
output:18060 (from adding the first three numbers)

one way is to for each building go left and right as long as the building is greater than the current building.
once you  have computed for all the buildings you can get the maximum
"""

from collections import defaultdict

higher = defaultdict(set)

def get_left_right_val_forward(hs, n, i, height):
    right = n + i + 1
    if right in higher[n]:
        height += hs[n]
        return height
    left = n + i
    if right<len(hs):
        if hs[right] > hs[n]:
            higher[n].add(right)
            height += hs[n]
            return height
        elif hs[right] == hs[n]:
            higher[n].add(right)
            higher[right].add(n)
            height += hs[n]
            return height
        else:
            higher[right].add(n)

def get_left_right_val_backward(hs, n, i, height):
    #__import__('pudb').set_trace()
    left = n - i - 1
    if left in higher[n]:
        height += hs[n]
        return height
    right = n - i
    if left >= 0:
        if hs[left] > hs[n]:
            higher[n].add(left)
            height += hs[n]
            return height
        if hs[left] == hs[n]:
            higher[n].add(left)
            higher[left].add(n)
            height += hs[n]
            return height
        else:
            higher[left].add(n)

def get_greatest_height(hs, n, curr_max):
    if n == 0:
        return curr_max

    i = 0
    height = hs[n]

    # forward
    _height = get_left_right_val_forward(hs, n, i, height)
    while _height is not None:
        height = _height
        i += 1
        _height = get_left_right_val_forward(hs, n, i, _height)

    # backward
    i = 0
    _height = get_left_right_val_backward(hs, n, i, height)
    while _height is not None:
        height = _height
        i += 1
        _height = get_left_right_val_backward(hs, n, i, _height)

    #print('higher',higher)

    # get the running max
    curr_max = max(curr_max, height)

    return get_greatest_height(hs, n-1, curr_max)


def main(hs):
    #print(hs)
    print(get_greatest_height(hs, len(hs)-1, 0))
    #print(higher)
    #print("%"* 10)

higher = defaultdict(set)
main([3,2,3])

higher = defaultdict(set)
main([11,11,10,10,10])

higher = defaultdict(set)
main([1,2,3,4,5])
