from inspect import currentframe, getframeinfo

def modulus(large_num):
    divisor = 1000007
    return large_num & (divisor-1)

print(modulus(23456788999999))
print(modulus(123))


def swap_ints(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


print(swap_ints(1, 2))

# lonely integer
# https://www.hackerrank.com/challenges/lonely-integer/problem

from functools import reduce

def find_lonely_integer(list):
    return reduce(lambda a, b: a^b, list, 0)

print(find_lonely_integer([1,1,2]))
print(find_lonely_integer([0,0,1,2,1]))


# https://www.hackerrank.com/challenges/counter-game/problem

import math

def invertBits(num):

    # calculating number of bits in the number
    x = int(math.log2(num)) + 1

    # Inverting the bits one by one
    for i in range(x):
        num = (num ^ (1 << i))
        print(num)

    return num

print(bin(10))
print(invertBits(10))


from itertools import cycle
from math import log2

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

def check_power_2(x):
    if x == 2:
        return True
    x = int(x)
    return x & (x-1) == 0

def get_lower_2_pow(x):
    x = int(x)
    size = int(log2(x))
    last2 = 1 << size
    return x - last2

def play_counter_game(x, players, counter=None):
    if counter is None and x == 1:
        return "Richard"

    if counter is None:
        counter = x

    curr_player = next(players)
    if counter is 1:
        return curr_player

    if check_power_2(counter):
        curr_val = int(counter/2)
        print(curr_player, curr_val, get_linenumber())
        if curr_val == 1:
            return  curr_player
        return play_counter_game(x, players, counter=curr_val)
    else:
        curr_val = get_lower_2_pow(counter)
        print(curr_player, curr_val, get_linenumber())
        if curr_val == 1:
            return curr_player
        return play_counter_game(x, players, counter=curr_val)


def counter_game(counter):
    players = cycle(["Loise", "Richard"])
    return play_counter_game(counter, players)

print(counter_game(6))

