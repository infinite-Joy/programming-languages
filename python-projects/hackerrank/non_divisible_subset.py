# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import itertools

def check_two_comb(curr_comb, k):
    processed = {}
    for i, j in itertools.combinations(curr_comb, 2):
        if (i, j) not in processed:
            if (i + j) % k == 0:
                return False
            processed[(i, j)] = True
    return True


def all_comb(S, k):
    for comb_count in range(len(S), 1, -1):
        for comb in itertools.combinations(S, comb_count):
            if check_two_comb(comb, k):
                return comb_count


print(all_comb([1, 7, 2, 4], 3))
print(all_comb([278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436], 7))
print(all_comb([1,2,3,4,5], 1))
