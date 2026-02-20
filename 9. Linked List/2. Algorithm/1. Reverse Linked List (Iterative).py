
def reverse_list(head):
    current=head
    prev=None
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    
    return prev



