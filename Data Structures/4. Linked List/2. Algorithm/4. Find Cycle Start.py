def detect_cycle(head):
    """
    Find where cycle begins
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    # Find meeting point
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
