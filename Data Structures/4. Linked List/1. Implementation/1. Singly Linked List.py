class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def insert_at_beginning(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def insert_at_end(self, data):
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=new_node
        self.size+=1
    def insert_at_position(self, data, position):
        new_node=Node(data)
        if position<0 or position>self.size:
            raise IndexError("Position out of bound!!")
        if position==0:
            self.head=new_node
        itr=self.head
        for i in range(position-1):
            itr=itr.next
        new_node.next=itr.next
        itr.next=new_node
        self.size+=1
    def delete_at_beginning(self):
        if self.is_empty():
            raise Exception("List is empty")
        data=self.head.data
        self.head=self.head.next
        self.size=-1
        return data
    def delete_at_end(self):
        if self.is_empty():
            raise Exception("List is empty!!")
        if self.head.next is None:
            data=self.head.data
            self.head=None
            self.size-=1
            return data
        itr=self.head
        while itr.next.next:
            itr=itr.next
        data=itr.next.data
        itr.next=None
        self.size-=1
        return data
        
    def delete_at_position(self, position):
        if position<0 or position>self.size():
            raise IndexError("Index is out of range!!")
        if position==0:
            data=self.head.data
            self.head=None
            self.size-=1
            return data
        itr=self.head
        for _ in range(position-1):
            itr=itr.next
        data=itr.next.data
        itr.next=None
        self.size-=1
        return data
            
    def delete_by_value(self, value):
        if self.is_empty():
            raise Exception("List is empty!!")
        if self.head.data==value:
            self.head=self.head.next
            size-=1
            return True
        itr=self.head
        for _ in range(self.size()-1):
            data=itr.next.data
            if data==value:
                itr.next=itr.next.next
                size-=1
                return True
        return False

    def search(self, value):
        itr=self.head
        position=0
        for _ in range(self.size()):
            if itr.data==value:
                return position
            else:
                itr=itr.next
                position+=1
        return -1
    def get(self, position):
        if position<0 or position>self.size:
            raise IndexError("Position is out of range")
        itr=self.head
        for _ in range(position):
            itr=itr.next
        return itr.data

    def reverse(self):
        prev=None
        itr=self.head
        while itr:
            next_node=itr.next
            itr.next=prev
            prev=itr
            itr=next_node
        self.head=prev
        return prev

    def display(self):
        if self.is_empty():
            print("Empty list")
            return
        itr=self.head
        elements=[]
        while itr:
            elements.append(str(itr.data))
            itr=itr.next

        print("-> ".join(elements) + "-> None")

    def to_list(self):
        itr=self.head
        elements=[]
        while itr:
            elements.append(itr.data)
        return elements
        


    # Usage Example:
ll = SinglyLinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
ll.display()  # 0 -> 1 -> 2 -> 3 -> None
ll.reverse()
ll.display()  # 3 -> 2 -> 1 -> 0 -> None

