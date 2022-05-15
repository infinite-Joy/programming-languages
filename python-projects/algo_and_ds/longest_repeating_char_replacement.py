

def longest_repeating_char_repl(string):
    longest_substring = 0
    i = 0
    counts = {}
    maxelem = None
    maxcount = 0
    for j in range(len(string)):
        incoming = string[j]
        if incoming not in counts:
            counts[incoming] = 1
        else:
            counts[incoming] += 1
        maxcount = max(maxcount, counts[incoming])
        if maxcount == counts[incoming]:
            maxelem = incoming
        # do the condition check
        if (j - i + 1 - counts[maxelem] <= k):
            longest_substring = max(longest_substring, j - i + 1)
        while i < j and (j - i + 1 - counts[maxelem] > k):
            print('while loop', i, j, j - i + 1, counts[maxelem])
            longest_substring = max(longest_substring, j - i)
            outgoing = string[i]
            if outgoing == maxelem:
                counts[maxelem] -= 1
            i += 1

        print(i, j, j - i + 1, counts)
    
    return longest_substring

s = "ABAB"
k = 2
print('answer', longest_repeating_char_repl(s))

s = "AABABBA"
k = 1
print('answer', longest_repeating_char_repl(s))