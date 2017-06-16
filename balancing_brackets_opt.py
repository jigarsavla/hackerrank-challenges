# FUNDAMENTALS: stack example
# PROBLEM: balancing brackets
# Optimized 

lass Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def print(self):
        print(self.items)

def is_matched(expression):
    pairs = {'{':'}', '[':']', '(':')'}
    stack = Stack()
    for char in expression:
        if char in pairs:
            stack.push(char)
            #stack.print()
        elif stack.isEmpty() or (char != pairs[stack.pop()]):
            #stack.print()
            #print("stack empty", stack.isEmpty())
            return False

    # handles null case for expression and for regular cases, where we need the stack to be empty
    return stack.isEmpty()
            


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")