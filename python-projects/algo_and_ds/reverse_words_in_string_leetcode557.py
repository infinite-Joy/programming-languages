"""

https://www.careercup.com/question?id=5106757177180160

https://leetcode.com/problems/reverse-words-in-a-string-iii/

Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted.
Example, for this input string

@"the boy ran"

the output would be

@"eht yob nar"

Tell the complexity of the solution.

basically have two pointers

while i is space and j is space: increment botj


"""

def reverse(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

def reverse_words(string):
    string = list(string)
    i = 0
    j = 1
    while j < len(string):
        print(i, j)
        # if i and j both are chars
        if string[i] != ' ' and string[j] != ' ':
            j += 1

        # if i is space and j is non space, word starting
        elif string[i] == ' ' and string[j] != ' ':
            i = j
            j += 1

        # if i is non space and j is space. word ending
        elif (string[i] != ' ' and string[j] == ' '):
            reverse(string, i, j-1)
            i = j
            j += 1

        # if i and j is space
        else: #string[i] == ' ' and string[j] == ' ':
            i += 1
            j += 1

    reverse(string, i, j-1)

    return "".join(string)

string = "the boy ran"
print(reverse_words(string))
