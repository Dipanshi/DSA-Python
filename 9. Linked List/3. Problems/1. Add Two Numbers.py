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

def add_two_numbers(l1, l2):
    """
    Add two numbers represented as linked lists
    Time: O(max(n, m)), Space: O(max(n, m))
    """
    dummy=ListNode(0)
    current=dummy
    carry=0

    while l1 or l2 or carry:
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0
        total = val1+val2+carry
        carry=total//10
        current.next=ListNode(total%10)

        current=current.next
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None

    return dummy.next

l1= create_linked_list([1,2,3,5,6,7])
l2= create_linked_list([2,3,5,6,7])
print_list(add_two_numbers(l1,l2))







    