BACKTRACk = 0
def find_values(n, values, summ, count, possibilities):
    global BACKTRACk
    print(n, values, summ, count)
    for i in values:
        summ += i
        possibilities.append(i)
        if sum(possibilities) == n:
            print(possibilities)
        if sum(possibilities) < n:
            count += find_values(n, values, summ, count, possibilities)
            possibilities.pop()
            BACKTRACk += 1
            summ -= i
        else:
            return count
    return count


def stepPerms(n):
    values = list(range(1, n+1))
    count = find_values(n, values, 0, 0, [])
    return count


print('ans', stepPerms(1))
print(BACKTRACk)
BACKTRACk = 0

print('ans', stepPerms(2))
print(BACKTRACk)
BACKTRACk = 0

#print('ans', stepPerms(3))
#print(BACKTRACk)
#BACKTRACk = 0
