#https://www.hackerrank.com/test/61sq9qfa63d/questions/9iji81pabbk

def fibonacci(n):

    # Write your code here.
    zero = 0
    one = 1
    two = zero + one

    if n == 0: return zero
    if n == 1: return one
    if n > 1:
        for i in range(2, n+1):
            fib = zero + one
            zero = one
            one = fib
    return fib


n = int(input())
