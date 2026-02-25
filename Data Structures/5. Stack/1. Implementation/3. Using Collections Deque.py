from collections import deque

# Deque is more efficient than list for stacks
stack = deque()

stack.append(1)      # Push
stack.append(2)
stack.append(3)
print(stack.pop())   # Pop: 3
print(stack[-1])     # Peek: 2