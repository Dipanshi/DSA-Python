

def get_intersection_node(headA, headB):
    """
    Find intersection point of two lists
    Time: O(n + m), Space: O(1)
    """
    if not headA or not headB:
        return None
    
    hA=headA
    hB=headB
    while hA!=hB:
        hA=hA.next if hA else hB.next
        hB=hB.next if hB else hA.next

    return hA


    