class RandomNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def copy_random_list(head):
    """
    Deep copy list with random pointers
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    
    # Create new nodes interleaved with original
    current = head
    while current:
        new_node = RandomNode(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Set random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Separate lists
    dummy = RandomNode(0)
    current = head
    copy_current = dummy
    
    while current:
        copy_current.next = current.next
        current.next = current.next.next
        
        copy_current = copy_current.next
        current = current.next
    
    return dummy.next