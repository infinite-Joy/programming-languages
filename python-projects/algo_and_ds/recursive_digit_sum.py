def super_digit_rec(number):
    if len(number)==1 and "0"<=number<="9":
        return int(number)
    sup_dig = sum(map(int, number))
    return super_digit_rec(str(sup_dig))

def main(n, k):
    n = str(n)
    sup_dig = sum(map(int, n)) * k
    sup_dig = str(sup_dig)
    return super_digit_rec(sup_dig)

print(main(9875, 1))
print(main(148, 3))
