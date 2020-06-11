# https://www.hackerrank.com/contests/techcb2k18v1/challenges/google-google
import math

number_of_test_cases = int(input())
#print(number_of_test_cases)
for i in range(number_of_test_cases):
    number_of_hrs = int(input())
    #print(number_of_hrs)
    heights_of_hrs = input().split()
    heights_of_hrs = [int(x) for x in heights_of_hrs]
    #print(heights_of_hrs)
    count_of_students = input().split()
    count_of_students = [int(x) for x in count_of_students]
    #print(count_of_students)

    #print(sorted(heights_of_hrs))
    #print(sorted(count_of_students))

    #print('answer')
    print("Case {}:{}".format(i+1, int(sum([math.fabs(x - y) for x, y in zip(sorted(heights_of_hrs), sorted(count_of_students))]))))

