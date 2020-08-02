"""
https://leetcode.com/problems/multiply-strings/
this can be done using a single pass and an arr
basically read through the first number and then
store the accumulate of the number in an array of 1-9
then for the second number convert to the integer and then do a running sum
ord(“1”) is 49
and then we can find the multiplication
======================
"""

def multiply(num1, num2):
    """
    time complexity is O(len(num1) + len(num2))
    space complexity O(min(len(num1, num2)))
    """
    if len(num2) < len(num1):
        num1, num2 = num2, num1
    # convert num1 to integer
    int1 = 0
    for v in num1:
        num = ord(v) % ord('0')
        int1 = int1*10 + num
    # create the multiples and store in array
    ints = [0 for _ in range(10)]
    for i in range(1, 10):
        ints[i] = ints[i-1] + int1
    # do piece by piece multiplication
    multiple = 0
    for v in num2:
        num = ord(v) % ord('0')
        multiple = multiple * 10 + ints[num]
    return (str(multiple))

print(multiply("2", "3"))
print(multiply("123", "456"))
