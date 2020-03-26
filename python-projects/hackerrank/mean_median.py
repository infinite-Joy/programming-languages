import math

number_of_elements = int(input())
elements = [int(x) for x in input().split()]

mean = sum(elements)/number_of_elements
print(mean)

elements = sorted(elements)
if number_of_elements%2==0:
    half = int(number_of_elements/2)
    middle1, middle2 = half-1, half
    median = (elements[middle1] + elements[middle2])/2
    print(median)
else:
    middle_elem = int(number_of_elements/2)
    median = elements[middle_elem]
    print(median)

frequency_distribution = [(x, elements.count(x)) for x in elements]
max_freq = max([x[1] for x in frequency_distribution])

def find_mode(frequency_distribution, max_freq):
    for elem, c in frequency_distribution:
        if c == max_freq:
            return elem

print(find_mode(frequency_distribution, max_freq))

