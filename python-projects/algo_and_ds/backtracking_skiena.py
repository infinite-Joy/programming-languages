"""
backtracking general and implementation for all subsets using skiena
"""

from typing import List

FINISHED = False


def is_a_solution(arr, k, data) -> bool:
    # application specific
    return k == data


def process_solution(arr, k, data):
    # application specific
    print(",".join(["{}".format(i) for i in range(1,k+1) if arr[i] is True]))



def construct_candidates(arr, k, data):
    # application specific
    candidates = [True, False]
    return candidates


def make_move(arr, k, data):
    pass


def unmake_move(arr, k, data):
    pass


def backtrack(arr: List[int], k: int, data: int):
    """
    Backtracking general algorithm as per skiena
    """
    #print(arr, k, data)
    if is_a_solution(arr, k, data):
        process_solution(arr, k, data)
    else:
        k += 1
        candidates = construct_candidates(arr, k, data)
        for candidate in candidates:
            arr[k] = candidate
            make_move(arr, k, data)
            backtrack(arr, k, data)
            unmake_move(arr, k, data)
            if FINISHED is True:
                return

def generate_subsets(n):
    arr = [False for _ in range(n+1)]
    backtrack(arr, 0, n)

generate_subsets(3)
