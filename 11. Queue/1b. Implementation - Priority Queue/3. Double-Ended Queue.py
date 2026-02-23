from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0
    
    def add_front(self, item):
        """Add to front - O(1)"""
        self.items.appendleft(item)
    
    def add_rear(self, item):
        """Add to rear - O(1)"""
        self.items.append(item)
    
    def remove_front(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.popleft()
    
    def remove_rear(self):
        """Remove from rear - O(1)"""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop()
    
    def peek_front(self):
        """Peek front - O(1)"""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items[0]
    
    def peek_rear(self):
        """Peek rear - O(1)"""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items[-1]
    
    def size(self):
        """Get size - O(1)"""
        return len(self.items)

# Usage:
dq = Deque()
dq.add_front(1)
dq.add_rear(2)
dq.add_front(0)
print(dq.remove_front())  # 0
print(dq.remove_rear())   # 2