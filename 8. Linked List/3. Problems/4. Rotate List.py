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

def rotate_right(head, k):
    """
    Rotate list to the right by k places
    Time: O(n), Space: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    
    # Find length and last node
    length = 1
    last = head
    while last.next:
        last = last.next
        length += 1
    
    # Make it circular
    last.next = head
    
    # Find new tail (length - k % length - 1)
    k = k % length
    steps_to_new_tail = length - k - 1
    
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

l1=create_linked_list([1,2,4,5,6])
print_list(rotate_right(l1,9))
