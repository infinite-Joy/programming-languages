# https://www.hackerrank.com/challenges/balanced-brackets/problem

from collections import deque
class Stack:
    def __init__(self):
        self._stack = deque([])
    def put(self, e):
        self._stack.append(e)
    def get(self):
        try:
            return self._stack.pop()
        except IndexError as e:
            raise e
    def is_empty(self):
        return bool(self._stack) == False

def check_balanced(brackets):
    opening_closing = {'{': '}', '[': ']', '(': ')'}
    call_stack = Stack()
    for b in brackets:
        if b in opening_closing:
            call_stack.put(b)
        else:
            try:
                last_bracket = call_stack.get()
            except IndexError:
                return "NO"
            if opening_closing[last_bracket] == b:
                pass     # check is passed
            else:
                return 'NO'
    if not call_stack.is_empty():
        return "NO"
    return 'YES'

print(check_balanced("}][}}(}][))]"))
print(check_balanced("[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}"))
