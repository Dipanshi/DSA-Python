from collections import deque

class RecentCounter:
    """
    Count requests in last 3000ms
    """
    def __init__(self):
        self.requests = deque()
    
    def ping(self, t):
        """Add request and count recent - O(1) amortized"""
        self.requests.append(t)
        
        # Remove old requests
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        
        return len(self.requests)

# Usage:
# rc = RecentCounter()
# print(rc.ping(1))     # 1
# print(rc.ping(100))   # 2
# print(rc.ping(3001))  # 3
# print(rc.ping(3002))  # 3

dq=deque([1,2,3,5,7,8,9])
dq.rotate(-1)
print(dq)