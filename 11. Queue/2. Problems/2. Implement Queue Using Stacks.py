class MyQueue:
    """
    Implement queue using two stacks
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x):
        """Push element - O(1)"""
        self.stack1.append(x)
    
    def pop(self):
        """Pop element - O(1) amortized"""
        self._move()
        return self.stack2.pop()
    
    def peek(self):
        """Peek front - O(1) amortized"""
        self._move()
        return self.stack2[-1]
    
    def empty(self):
        """Check if empty - O(1)"""
        return not self.stack1 and not self.stack2
    
    def _move(self):
        """Move elements from stack1 to stack2"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())