class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        """Insert at beginning - O(n)"""
        new_node = Node(data)
        
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert at end - O(n)"""
        new_node = Node(data)
        
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        self.size += 1
    
    def delete_node(self, value):
        """Delete node with value - O(n)"""
        if self.head is None:
            return False
        
        current = self.head
        prev = None
        
        # Check if head node has the value
        if current.data == value:
            # Find last node
            while current.next != self.head:
                current = current.next
            
            # If only one node
            if self.head == current:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            
            self.size -= 1
            return True
        
        # Search for the node
        prev = self.head
        current = self.head.next
        
        while current != self.head:
            if current.data == value:
                prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        
        return False
    
    def display(self):
        """Display list - O(n)"""
        if self.head is None:
            print("Empty list")
            return
        
        current = self.head
        elements = []
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements) + " -> (back to head)")

# Usage:
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.display()  # 1 -> 2 -> 3 -> (back to head)