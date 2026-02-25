class ListNode:
    def __init__(self, val,next=None):
        self.val=val

def Find_cycle_start(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return slow.next.val
    return None       

# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2   # <-- cycle here

head = node1

print(Find_cycle_start(head))
    