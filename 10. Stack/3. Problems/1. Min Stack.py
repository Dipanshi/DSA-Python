class MinStack:
    """
    Stack with O(1) min operation
    """
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,data):
        self.stack.append(data)
        if not self.min_stack or data<self.min_stack[-1]:
            self.min_stack.append(data)
    def pop(self):
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]


# Usage:
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.get_min())  # -3
ms.pop()
print(ms.get_min())  # -2