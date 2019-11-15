# Enter your code here. Read input from STDIN. Print output to STDOUT

def weighted_mean(values, weights):
    weighted_values = [x*y for x, y in zip(values, weights)]
    return sum(weighted_values)/sum(weights)

if __name__ == '__main__':
    N = int(input())
    values = [int(x) for x in input().split()]
    weights = [int(x) for x in input().split()]
    print(weighted_mean(values, weights))
