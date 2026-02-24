from collections import deque

class FirstUnique:
    """
    Find first unique character in stream
    """
    def __init__(self):
        self.queue = deque()
        self.count = {}
    
    def add(self, char):
        """Add character - O(1)"""
        self.count[char] = self.count.get(char, 0) + 1
        self.queue.append(char)
    
    def get_first_unique(self):
        """Get first unique - O(n) worst case"""
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        
        return self.queue[0] if self.queue else None

# Usage:
fu = FirstUnique()
fu.add('a')
fu.add('b')
fu.add('a')
print(fu.get_first_unique())  # 'b'