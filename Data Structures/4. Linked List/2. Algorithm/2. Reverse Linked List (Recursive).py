def reverse_list_recursive(head):
    if not head or not head.next:
        return head    
    new_head=reverse_list_recursive(head.next)
    head.next.next=head
    head.next=None

    return new_head