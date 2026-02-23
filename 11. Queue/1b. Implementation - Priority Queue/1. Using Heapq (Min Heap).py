import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.heap) == 0
    
    def push(self, item, priority):
        """Add item with priority - O(log n)"""
        heapq.heappush(self.heap, (priority, item))
    
    def pop(self):
        """Remove highest priority item - O(log n)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return heapq.heappop(self.heap)[1]
    
    def peek(self):
        """Get highest priority item - O(1)"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.heap[0][1]
    
    def size(self):
        """Get size - O(1)"""
        return len(self.heap)

# Usage:
pq = PriorityQueue()
pq.push("task1", 3)
pq.push("task2", 1)  # Higher priority
pq.push("task3", 2)
print(pq.pop())  # task2 (lowest number = highest priority)