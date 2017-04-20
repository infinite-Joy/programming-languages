"""
fibonacci
"""

def f(n):
    def fib(n):
        a, b = 0, 1
          for _ in range(n):
            yield a
            a, b = b, a + b
    return list(fib(n))[-1]
