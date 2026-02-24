class MultiNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.child = None
    
def create_multilevel_list():
    # Level 1
    n1 = MultiNode(1)
    n2 = MultiNode(2)
    n3 = MultiNode(3)
    n4 = MultiNode(4)
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    # Level 2 (child of 3)
    n7 = MultiNode(7)
    n8 = MultiNode(8)
    n9 = MultiNode(9)
    n7.next = n8
    n8.prev = n7
    n8.next = n9
    n9.prev = n8
    n3.child = n7
    # Level 3 (child of 8)
    n11 = MultiNode(11)
    n12 = MultiNode(12)
    n11.next = n12
    n12.prev = n11
    n8.child = n11
    return n1
def print_multilevel(head, level=0):
    current = head
    while current:
        print("  " * level + str(current.val),)
        if current.child:
            print_multilevel(current.child, level + 1)
        
        current = current.next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None") 

###########################################################

def flatten(head):
    """
    Flatten multilevel doubly linked list
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    stack=[]
    current=head
    while current:
        if current.child:
            if current.next:
                stack.append(current.next)
                current.next=current.child
                current.child=None
        if not current.next and stack:
            next_node=stack.pop()
            current.next=next_node
            next_node.prev=current
        
        current=current.next
    return head

n1=create_multilevel_list()
print_multilevel(n1)
print_list(flatten(n1))