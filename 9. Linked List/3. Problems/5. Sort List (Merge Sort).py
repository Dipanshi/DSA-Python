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
def merge_two_lists(left, right):
    if not left and not right:
        return None
    dummy=ListNode(0)
    current=dummy
    while left and right:
        if left.val<right.val:
            current.next=left
            left=left.next
        else:
            current.next=right
            right=right.next
        current=current.next

    current.next= left if left else right

    return dummy.next

#############################################
def sort_list(head):
    """
    Sort linked list using merge sort
    Time: O(n log n), Space: O(log n)
    """
    if not head or not head.next:
        return head
    
    # Find middle
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Split
    prev.next = None
    
    # Sort both halves
    left = sort_list(head)
    right = sort_list(slow)
    
    # Merge
    return merge_two_lists(left, right)


l1= create_linked_list([1,2,4,7,3,7,8,1])
print_list(sort_list(l1))