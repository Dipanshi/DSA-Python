class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedStack:
    def __init__(self):
        self.top=None
        self.size=0
    def is_empty(self):
        """Check if empty - O(1)"""
        return self.top is None
    def push(self, data):
        """Push element - O(1)"""
        new_node=StackNode(data)
        new_node.next=self.top
        self.top=new_node
        self.size+=1
    def pop(self):
        """Pop element - O(1)"""
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    def peek(self):
        """Peek top element - O(1)"""
        return self.top.data
    def get_size(self):
        """Get size - O(1)"""
        return self.size
    
stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())   # 3
print(stack.peek())  # 2