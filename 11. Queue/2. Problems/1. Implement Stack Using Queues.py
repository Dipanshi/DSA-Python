from collections import deque

class MyStack:
    """
    Implement stack using two queues
    """
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        """Push element - O(n)"""
        self.q2.append(x)
        
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        """Pop element - O(1)"""
        return self.q1.popleft()
    
    def top(self):
        """Get top element - O(1)"""
        return self.q1[0]
    
    def empty(self):
        """Check if empty - O(1)"""
        return len(self.q1) == 0