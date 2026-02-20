def has_cycle(head):
    """
    Detect cycle using fast & slow pointers
    Time: O(n), Space: O(1)
    """
    if not head:
        return False
    left=right=head
    while right and right.next:
        left=left.next
        right=right.next.next
        if left==right:
            return True
    
    return False


        