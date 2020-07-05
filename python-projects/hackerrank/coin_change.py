# coin change problem
# https://www.hackerrank.com/challenges/coin-change/problem

#def coin_conf(N, coins, n, c=0):
#    while n > 0:
#        print(N, coins, n, c)
#        coin = coins[n]     # 3, 2, 1
#        if coin <= N:
#            rem = N%coin    # rem 1, 0, 0
#            if rem == 0:    # not valid, valid
#                c+=1    # NA, NA, 1
#                left = N - coin # 0
#                if left == 0: # NA, this will work
#                    c = coin_conf(N, coins[:-1], len(coins[:-1])-1, c)
#                    return c # this is returned
#                c = coin_conf(left, coins, n-1, c)
#            else:        # goes here
#                c = coin_conf(rem, coins, n-1, c) # 1, [1,2,3], 1, 0
#        n = n-1 # 0
#
#    return c
#
#print(coin_conf(4, [1,2,3], 2))

from itertools import chain, combinations, combinations_with_replacement, permutations, product
from functools import lru_cache

def powerset(coins):
    xs = list(coins)
    return chain.from_iterable(combinations(xs, n) for n in range(1, len(xs)+1))

#for i in powerset([1,2,3]):
#    print(i)


coin_change_possible_map = {}

@lru_cache()
def possible(n, divisors):
    lowest_num = divisors[0]
    possible_divisors = n//lowest_num
    xs = list(range(1, possible_divisors+1))
    for dividends  in product(xs, repeat=len(divisors)):
        summ = [i*j for i, j in zip(divisors, dividends)]
        if sum(summ) == n:
            return True

#print(possible(10, (2,3)))
#print(possible(10, (2,3,5,6)))
#print(possible(10, (2,6)))


@lru_cache()
def coin_change_possible(N, coins):
    #print(N, coins)
    last_coin = coins[-1]
    if last_coin > N:
        return -1
    if len(coins) == 1:
        return N % last_coin
    else:
        diff = N % last_coin
        if diff == 0:
            diff = N - last_coin
        return coin_change_possible(diff, coins[:-1])

#print(coin_change_possible(4, (1,)))
#print(coin_change_possible(4, (2,)))
#print(coin_change_possible(4, (3,)))
#print(coin_change_possible(4, (1, 2)))
#print(coin_change_possible(4, (2, 3)))
#print(coin_change_possible(4, (1,2,3)))

def find_ways(n, c):
    #rem = [1 if coin_change_possible(n, i)==0 else 0 for i in powerset(c)]
    #return sum(rem)
    summ = 0
    c = sorted(c)
    for i in powerset(c):
        print(i)
        rem = possible(n, i)
        print(rem)
        print("#"*10)
        if rem is True:
            summ += 1
    return summ


#print(find_ways(4, [1,2,3]))
print(find_ways(10, [2,5,3,6]))
