import sys

def is_balanced(sentence):
    stack = []
    for char in sentence:
        if char in "([":  
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    print(is_balanced(line))
