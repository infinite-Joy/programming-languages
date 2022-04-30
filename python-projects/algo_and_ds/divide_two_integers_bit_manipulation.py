"""
This is sort of like binary search

bit manipulation


"""



def divide(dividend: int, divisor: int) -> int:
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    sign = 1
    if dividend > 0 and divisor > 0:
        sign = 1
    elif dividend < 0 and divisor < 0:
        sign = 1
    else:
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    ans = 0
    shift = 0
    while dividend >= divisor:
        temp = divisor
        m = 1
        while temp <= dividend:
            # print(temp, dividend)
            temp <<= 1
            m <<= 1
        temp >>= 1
        m >>= 1
        ans += m
        dividend -= temp
        # print(32, dividend)
    if sign < 0:
        return 0 - ans
    return ans


print(divide(10, 3))