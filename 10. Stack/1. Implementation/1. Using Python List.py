class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items)==0
    def push(self, item):
        """Add item to top - O(1)"""
        self.items.append(item)
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise Exception("The Stack is empty")
        return self.items.pop()
    def peek(self):
        """Return top item without removing - O(1)"""        
        if self.is_empty():
            raise Exception("The Stack is empty")
        return self.items[-1]
    def size(self):
        """Return size of stack - O(1)"""
        return len(self.items)
    def display(self):
        """Display stack - O(n)"""
        print(f"Stack: {self.items}")

# Usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3
print(stack.peek())  # 2

