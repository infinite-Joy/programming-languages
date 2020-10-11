from array import array

def print_prime_numbers(n):
    primes = array('l', [0 for _ in range(n + 1)])
    for i in range(2, n):
        if primes[i] == 0:
            print(i)
            multipliers = 2
            while i * multipliers < n:
                primes[i * multipliers] = 1
                multipliers += 1

print_prime_numbers(100)
