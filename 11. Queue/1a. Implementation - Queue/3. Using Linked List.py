class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return self.front is None
    
    def enqueue(self, data):
        """Add to rear - O(1)"""
        new_node = QueueNode(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return data
    
    def get_front(self):
        """Get front element - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data
    
    def get_size(self):
        """Get size - O(1)"""
        return self.size