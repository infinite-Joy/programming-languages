# reference https://practice.geeksforgeeks.org/tracks/DSASP-Mathematics/?batchId=154#

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


print(is_prime(20988936657440586486151264256610222593863921))
