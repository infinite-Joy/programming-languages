#https://www.hackerrank.com/contests/projecteuler/challenges/euler244/problem

letter_code = {"L": 76, "R": 82, "U": 85, "D": 68}


def get_checksum(seq, i=0, checksum=0):
    checksum = (checksum * 243 + letter_code[seq[i]]) % 100000007
    i += 1
    if i >= len(seq):
        return checksum
    return get_checksum(seq, i, checksum)

print(get_checksum("LULUR"))



