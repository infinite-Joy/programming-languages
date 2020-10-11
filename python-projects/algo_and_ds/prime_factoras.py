# find the prime factors based on the geeks for geeks tut

from math import sqrt
def is_prime(n):
    if n == 1: return 1
    if n == 2: return True
    if n == 3: return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)), 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

def print_prime_factors(n):
    print("printing prime factors of {}".format(n))
    if n <= 1:
        return

    i = 2
    while n >= i * i:
        if is_prime(i):
            while n % i == 0:
                print(i)
                n /= i
        i += 1

    if n > 1:
        print(int(n))

print_prime_factors(450)
print_prime_factors(84)
