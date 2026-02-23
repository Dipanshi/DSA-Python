from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add to rear - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Get front element - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]
    
    def size(self):
        """Get size - O(1)"""
        return len(self.items)
    
    def display(self):
        """Display queue - O(n)"""
        print("Queue:", list(self.items))

# Usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.front())    # 2
q.display()