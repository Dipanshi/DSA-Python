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

def reverse_list(head):
    rev=None
    while head:
        next_node=head.next
        head.next=rev
        rev=head
        head=next_node
    return rev
#############################################

def is_palindrome(head):
    """
    Check if linked list is palindrome
    Time: O(n), Space: O(1)
    """
    if not head and not head.next:
        return False
    
    #middle item
    slow=fast=head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    
    #reverse second half
    second_half=reverse_list(slow)

    first=head
    second=second_half

    while second:
        if first.val!=second.val:
            return False
        else:
            first=first.next
            second=second.next

    slow.next=reverse_list(second_half)

    return True

ll=create_linked_list([1,2,2,3,2,4,1])
print(is_palindrome(ll))





    