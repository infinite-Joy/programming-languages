# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

N = int(input())
values = [int(x) for x in input().split()]

mean = sum(values)/N

distance_from_mean = [(v-mean) for v in values]
sq_distance_from_mean = [x**2 for x in distance_from_mean]
sigma_sq = sum(sq_distance_from_mean)/N
sigma = math.sqrt(sigma_sq)
print(round(sigma, 1))
