number_of_elements = int(input())
elements = [float(x) for x in input().split()]
frequencies = [int(x) for x in input().split()]

def find_expanded_elements(elements, frequencies):
    final_elements = []
    for e, f in zip(elements, frequencies):
        expandeds = [e]*f
        final_elements = final_elements + expandeds
    return final_elements

expanded_elements = find_expanded_elements(elements, frequencies)
elements = sorted(expanded_elements)
number_of_elements = len(elements)

def find_median(values):
    values = sorted(values)
    n = len(values)
    half = int(n/2)
    if n%2==0:
        median = (values[half-1] + values[half])/2
        return int(median)
    else:
        return values[half]

def lower_upper_halves(elements, number_of_elements):
    if number_of_elements%2 == 0:
        half = int(number_of_elements/2)
        first_half = elements[:half]
        second_half = elements[half:]
        return find_median(first_half), find_median(elements), find_median(second_half)
    else:
        half = int(number_of_elements/2)
        first_half = elements[:half]
        q2 = elements[half]
        second_half = elements[half+1:]
        return find_median(first_half), q2, find_median(second_half)


q1, q2, q3 = lower_upper_halves(elements, number_of_elements)
print(float(q3 - q1))

