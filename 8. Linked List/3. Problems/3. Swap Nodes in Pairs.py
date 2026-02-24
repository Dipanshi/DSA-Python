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

def swap_pairs(head):
    """
    Swap every two adjacent nodes
    Time: O(n), Space: O(1)
    """
    dummy=ListNode(0)
    dummy.next=head
    current=dummy

    while current.next and current.next.next:
        first=current.next
        second=current.next.next

        first.next=second.next
        second.next=first
        current.next=second

        current=first

    return dummy.next

l1=create_linked_list([1,2,4,5,6])
print_list(swap_pairs(l1))
