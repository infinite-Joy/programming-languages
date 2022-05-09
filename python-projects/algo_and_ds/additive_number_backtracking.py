def backtracking(num, i, prev1, prev2):
    # base
    print(i)
    if i >= len(num) - 2:
        if prev2 + prev1 == int(num[i]):
            print(prev2, prev1, num[i])
            return True
        else:
            return False
    
    # normal case
    for j in range(i, len(num)):
        sumval = int(num[i:j+1])
        if prev1 + prev2 == sumval and backtracking(num, j+1, sumval, prev1) is True:
            return True
        
def main(num):
    prev2 = int(num[0])
    prev1 = int(num[1])
    return backtracking(num, 2, prev1, prev2)

# print(main('123'))

# print(main('1235'))
print(main('199100199'))