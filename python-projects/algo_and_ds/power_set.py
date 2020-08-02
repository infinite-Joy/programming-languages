"""
https://leetcode.com/problems/subsets/
since this is finding the power set we cannot come less than 2n.
but we dont need to store all the output. we can just store the combination
we can store we are picking the item or not in the form of the combination
so basically for each combination,. find the set bits and then from the set bits are the indices of the combination
time complexity is O(n)
space complexity is O(1)

finding set bits
9 = 1010
9 = 1001
============
"""
def find_set_bits(n):
    count = []
    i = 0
    while n > 0:
        if n & 1 == 1:
            count.append(i)
        i += 1
        n = n >> 1
    return count

print(find_set_bits(5))
print(bin(5))

def power_set(nums):
    for n in range(2**(len(nums))):
        set_bits = find_set_bits(n)
        yield [nums[i] for i in set_bits]
def subsets(nums):
    sol = []
    for s in power_set(nums):
        sol.append(s)
    return sol

print(subsets([1,2,3]))

