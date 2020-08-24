"""
Here we find the implementation of the knuth morris pratt

the time complexity is O(n+m)
the space complexity is O(n)
where n is the substring and m is the larger element

"""

def prefix_array(substring):
    # the complexity is O(n)
    arr = [0 for _ in substring]
    i = 0
    j = 1
    while j < len(substring):
        # matching
        if substring[i] == substring[j]:
            i += 1
            arr[j] = i
            j += 1

        # the first character did not match
        elif i == 0:
            arr[j] = 0
            j += 1

        # not matchin
        else:
            i = arr[i-1]

    return arr

arr = 'acacabacacabacacac'
print(prefix_array(arr))

def substring_search(text, pattern):
    print(text)
    print(pattern)
    i = 0
    j = 0
    arr = prefix_array(pattern)
    print(arr)
    while i < len(text) and j < len(text):

        print(i, j, text[i], pattern[j])

        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            # charater didnt match -> backtrack
            j = arr[j-1]
            if j == 0:
                i += 1

        # the pattern matches, now return the first index
        if j == len(pattern):
            return i - len(pattern)

text = 'abcxabcdabcdabcy'
pattern = 'abcdabcy'
print(substring_search(text, pattern))

text = "THIS IS A TEST TEXT"
pattern = "TEST"
print(substring_search(text, pattern))
