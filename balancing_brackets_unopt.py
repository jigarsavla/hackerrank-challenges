# FUNDAMENTALS: stack example
# PROBLEM: balancing brackets
# Unoptimized. the 'stack' list can take in any character. 
# should constrain it by using Dicts's values as the ONLY input parameter.
# this Dict would be composed of the bracket pairs.

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

def is_matched(expression):
    stack = Stack()
    for char in expression:
        if ((char == '{') | (char =='[') | (char == '(') ): stack.push(char)
        if (char == '}') : 
            if (stack.pop() != '{') : return False
        if (char == ']') : 
            if (stack.pop() != '[') : return False
        if (char == ')') : 
            if (stack.pop() != '(') : return False

    if stack.isEmpty():
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

