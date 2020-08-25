"""

https://www.careercup.com/question?id=6321181669982208

Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. (Exclude the N+0=N)

For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

This can also be done using the dp approach

let n = 4

1
11
111, 12
1111, 121, 13
11111, 1211, 131, 14

time complexity: O(n2)
space is also:O(n)

i think will have to implement a backtracking soltion for this

"""

def generate_combs(n):
    if n <= 1:
        return n

    sol = [[]]
    for num in range(1, n):
        sol = [[1]+x for x in sol]
        sol.append([num+1])
        print(sol)
    return sol

print(generate_combs(4))
