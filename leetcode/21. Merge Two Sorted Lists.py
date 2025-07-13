# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(ll1, ll2):

    if not ll1 and not ll2:
        return None

    if not ll1 and ll2:
        return ll2
    
    if ll1 and not ll2:
        return ll1

    smaller = ll1 if ll1.val <= ll2.val else ll2
    bigger = ll1 if ll1.val > ll2.val else ll2
    merged_ll = smaller
    parent = None
    while smaller and bigger:
        if smaller.val > bigger.val:
            temp2 = bigger.next
            parent.next = bigger
            parent.next.next = smaller
            smaller = merged_ll
            bigger = temp2
        
        parent = smaller
        smaller = smaller.next

    temp = merged_ll
    while temp.next:
        temp = temp.next

    temp.next = bigger

    return merged_ll

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return merge(list1, list2)
        
