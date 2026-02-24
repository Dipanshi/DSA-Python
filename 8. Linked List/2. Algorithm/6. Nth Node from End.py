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

def nth_from_end(head, n):
    slow=fast=head
    for _ in range(n):
        if not fast:
            return None
        fast=fast.next
    
    while fast:
        slow=slow.next
        fast=fast.next

    return slow.val



ll_head=create_linked_list([1,2,3,4,5,6,7])
print(nth_from_end(ll_head,5))

    
