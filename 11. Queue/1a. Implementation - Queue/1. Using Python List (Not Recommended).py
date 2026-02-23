class queuelist:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        """Add to rear - O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Remove from front - O(n) - INEFFICIENT!"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0