    # Find middle node of linked list
    # Time: O(n), Space: O(1)

class ListNode:
    def __init__(self, val= 0,next=None):
        self.val=val
        self.next=next

def MidOfLinkedList(head):
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node5 = ListNode(10)
node6 = ListNode(6)


# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
head = node1

print(MidOfLinkedList(head))