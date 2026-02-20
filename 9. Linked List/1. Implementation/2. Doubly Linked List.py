class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.size+=1

    def insert_at_end(self, data):
        new_node=Node(data)
        if self.is_empty():
            self.head=self.tail=new_node
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
        self.size+=1
        
    def insert_at_position(self, data, position):
        new_node=Node(data)
        if position<0 or position>self.size:
            raise IndexError("Position is out of range")
        if position==0:
            self.insert_at_beginning(data) 
            return
        if position==self.size:
            self.insert_at_end(data)
            return
        itr=self.head
        for _ in range(position-1):
            itr=itr.next
        new_node.prev=itr
        new_node.next=itr.next.next
        itr.next.prev=new_node
        itr.next=new_node
        self.size+=1   

    def delete_at_beginning(self):
        if self.is_empty():
            raise Exception("Linked list is empty")
        data=self.head.data
        if self.head== self.tail:
            self.head=self.tail=None
        else:    
            self.head=self.head.next
            self.head.prev=None
        self.size-=1
        return data

    def delete_at_end(self):
        if self.is_empty():
            raise Exception("Linked list is empty")
        data = self.tail.data
        if self.tail==self.head:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.size-=1
        return data

    def delete_by_value(self, value):
        if self.is_empty():
            raise IndexError("List is empty")
        if self.head.data==value:
            data=self.delete_at_beginning()
            return data
        if self.tail.data==value:
            data=self.delete_at_end()
            return data
        itr=self.head
        while itr:
            if itr.data==value:
                itr.prev.next=itr.next
                itr.next.prev=itr.prev
                self.size-=1
                return itr.data
        return -1

    def display_forward(self):
        itr=self.head
        elements=[]
        if self.head is None:
            print("List is empty")
            return
        while itr:
            elements.append(str(itr.data))
            itr=itr.next
        print("-> ".join(elements) + "-> None")

    def display_backward(self):
        itr=self.tail
        elements=[]
        if self.head is None:
            print("List is empty")
            return
        while itr:
            elements.append(str(itr.data))
            itr=itr.prev
        print("-> ".join(elements) + "-> None")

# Usage:
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display_forward()   # 1 <-> 2 <-> 3 <-> None
dll.display_backward()  # 3 <-> 2 <-> 1 <-> None