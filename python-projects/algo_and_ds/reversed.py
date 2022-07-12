


def reversed(x):
    negative = -1 if x < 0 else 1
    x = abs(x)
    stack = []
    while x:
        digit = x % 10
        x = x // 10
        stack.append(digit)
    reversed = 0
    for digit in stack:
        reversed = 10 * reversed
        reversed += digit
    return negative * reversed


print(reversed(1534236469))