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

def merge_two_lists(l1, l2):
    dummy=ListNode(0)
    current=dummy
    while l1 and l2:
        if l1.val>l2.val:
            current.next=l2
            l2=l2.next
        else:
            current.next=l1
            l1=l1.next

        current=current.next
    current.next = l1 if l1 else l2

    return dummy.next

ll1=create_linked_list([1,3,4,6])
ll2=create_linked_list([2,4,5,6,7])
merge_head=merge_two_lists(ll1,ll2)
print_list(merge_head)


