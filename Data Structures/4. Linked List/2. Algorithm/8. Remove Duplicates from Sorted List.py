class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")
#############################################

def delete_duplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

ll=create_linked_list([1,2,2,4,4,4,4,5,5,6,7])
head=delete_duplicates(ll)
print_list(head)