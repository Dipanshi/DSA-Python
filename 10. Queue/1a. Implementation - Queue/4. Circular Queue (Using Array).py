class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return self.size == 0
    
    def is_full(self):
        """Check if full - O(1)"""
        return self.size == self.capacity
    
    def enqueue(self, item):
        """Add item - O(1)"""
        if self.is_full():
            raise Exception("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove item - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def get_front(self):
        """Get front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

# Usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())  # 1