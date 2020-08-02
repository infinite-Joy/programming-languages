def iterate(inputs, n=0, word=None):
    if word is None:
        word = []
    if n >= len(inputs):
        print(word)
    next_letter = inputs[n]
    if next_letter == " ":
        word = []
    else:
        word.append(next_letter)
        iterate(inputs, n+1, word)
        print(word)
    try:
        letter_after_that = inputs[n+1]
        if letter_after_that == " ":
            print(word)
    except KeyError:
        print(word)


letters = ['p', 'e', 'r', ' ', 'f', 'u', 'c']
print(iterate(letters))

def iterate_through(inputs):
    stack = []
    current_word = []
    for i in inputs:
        if i == " ":
            stack.append(current_word)
            current_word = []
        else:
            current_word.append(i)
    if current_word:
        stack.append(current_word)
    return stack

def work_on_stack(stack):
    while stack:
        print("".join(stack.pop()))

letters = ['p', 'e', 'r', ' ', 'f', 'u', 'c']
stack = iterate_through(letters)
print(stack)
work_on_stack(stack)
